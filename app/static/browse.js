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

	url = 'http://sukoshi:9201/garments/_search'

	$.ajax(url, {
            cache: false,
            dataType: 'json',
            type: 'POST',
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
                            $('<a href="#"><img src="/static/uploads/' + r_items[r]._source.pic_title + '" class="original"></a>')
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
                alert('yay')
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

        url = 'http://sukoshi:9201/garments/_search'
        var results;
        console.log('go')

        $.ajax(url, {
            cache: false,
            dataType: 'json',
            type: 'POST',
            data: data,
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
                            $('<a href="#"><img src="/static/uploads/' + r_items[r]._source.pic_title + '" class="original"></a>')
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
                alert('yay')
            });

            }
        });
    });
});


