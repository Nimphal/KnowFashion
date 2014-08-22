$(document).ready(function() {
    $('#clothing_type').select2({
	placeholder: "Clothing type",
	allowClear: true
	});

	$('#colour').select2({
	placeholder: "Colour",
	allowClear: true
	});

	$('#country').select2({
	placeholder: "Country",
	allowClear: true
	});

	$('#go').tooltip();

	url = current_scheme + '//' + current_domain + ':9201/garments/_search?size=100'
	r_items = []
	console.log(url);

	$.ajax(url, {
            cache: false,
            dataType: 'json',
            type: 'GET',
            success: function (data, status, jqXHR) {
                results = data;
                console.log( results );
                console.log( 'yes' );
                var r_items = [];
                for (var i=0; i<results.hits.hits.length; i++) {
                    r_items.push(results.hits.hits[i]);
                    };

                for (var r=0; r<r_items.length; r++) {
                    if(r_items[r]._source.pic_title) {
                        $('<div class=image-container></div>')
                        .append(
                            $('<a href="#"><img src="/static/uploads/' + r_items[r]._source.pic_title +'" class="original" data-color="' + r_items[r]._source.colour +'"data-country="' + r_items[r]._source.country + '"data-brand="' + r_items[r]._source.brand +'"data-clothingtype="' + r_items[r]._source.clothing_type + '"></a>')
                        )
                        .append(
                            $('<br>')
                        )
                        .append(
                            $('<span>' + r_items[r]._source.country + '</span>')
                        )
                        .appendTo('#image')

                    }

                };

            $('.image-container img').click(function() {
                $.colorbox({html:'<img src="' + $(this).prop('src') + '" style= "height: 400px; padding: 10px;"><div style="display: inline-block; font-size: 20px;"><span>' + '<br>' + $(this).attr('data-brand') + '<br>' + $(this).attr('data-color') +' ' + $(this).attr('data-clothingtype') + '<br> from ' + $(this).attr('data-country') + '</span></div>',
                            width: '500px',
                            height: '500px',
                            transition: 'elastic',
                            fadeOut: 200
                });
            });


            }
        });



    $('#go').click(function(event) {
        $("#image").html("");
        event.preventDefault();
        console.log('go');
        ct = $('#clothing_type').val()
        cl = $('#colour').val()
        brand = $('#brand').val().toLowerCase();
        country = $('#country').val().toLowerCase();

        data = '{"query":{"filtered":{"query":{"match_all":{}},"filter":{"bool":{"must":['

        if (country) {data = data + '{"term":{"country":"' + country + '"}}'};

        if (cl) {
            if (country) {
                data = data + ',{"term":{"colour":"' + cl + '"}}'
                } else {data = data + '{"term":{"colour":"' + cl + '"}}'}
                };

        if (ct) {
            if (cl || country) {
                data = data + ',{"term":{"clothing_type":"' + ct + '"}}'
                } else {data = data + '{"term":{"clothing_type":"' + ct + '"}}'}
            };

        if (brand) {
            if (cl || ct || country){
                data = data + ',{"term":{"brand":"' + brand + '"}}'
                } else {data = data + '{"term":{"brand":"' + brand + '"}}'}
            };

        /*
        var added_a_term = false;
        if (country) {
            if(added_a_term) { data = data + ',' }
            data = data + '{"term":{"country":"' + country + '"}}'
            added_a_term = true
        }

        if (cl) {
            if(added_a_term) { data = data + ',' }
            data = data + '{"term":{"colour":"' + cl + '"}}'
            added_a_term = true
        }

        if (ct) {
            if(added_a_term) { data = data + ',' }
            data = data + '{"term":{"clothing_type":"' + ct + '"}}'
            added_a_term = true
        }
        */

        data = data + ']}}}}}'
        console.log(data)

        url = current_scheme + '//' + current_domain + ':9201/garments/_search?size=100'
        var results;
        console.log('go')

        $.ajax(url, {
            cache: false,
            dataType: 'json',
            type: 'GET',
            data: data,
            success: function (data, status, jqXHR) {
                results = data;
                console.log( results );
                console.log( 'yes' );
                r_items = [];
                for (var i=0; i<results.hits.hits.length; i++) {
                    r_items.push(results.hits.hits[i]);
                    };

                for (var r=0; r<r_items.length; r++) {
                    if(r_items[r]._source.pic_title) {
                        $('<div class=image-container></div>')
                        .append(
                            $('<a href="#"><img src="/static/uploads/' + r_items[r]._source.pic_title +'" class="original" data-color="' + r_items[r]._source.colour +'"data-country="' + r_items[r]._source.country + '"data-brand="' + r_items[r]._source.brand +'"data-clothingtype="' + r_items[r]._source.clothing_type + '"></a>')
                        )
                        .append(
                            $('<br>')
                        )
                        .append(
                            $('<span>' + r_items[r]._source.country + '</span><br>')
                        )
                        .appendTo('#image')

                    }


                };
            $('.image-container img').click(function() {
                $.colorbox({html:'<img src="' + $(this).prop('src') + '" style= "height: 300px; padding: 10px;"><div style="display: inline-block; font-size: 20px;"><span>' + '<br>' + $(this).attr('data-brand') + '<br>' + $(this).attr('data-color') +' ' + $(this).attr('data-clothingtype') + '<br> from ' + $(this).attr('data-country') + '</span></div>',
                            maxWidth: '95%',
                            maxHeight: '95%',
                            transition: 'elastic',
                            fadeOut: 200,
                            reposition: false
                });


            });


            }
        });
    });
});



