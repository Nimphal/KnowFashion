$(document).ready(function() {
    $('#clothing_type').select2({
	placeholder: "Select clothing type"
	});

	$('#colour').select2({
	placeholder: "Select colour"
	});

	$('#country').select2({
	placeholder: "Select country"
	});

    $('#go').click(function(event) {
        event.preventDefault();
        console.log('go');
        ct = $('#clothing_type').val()
        cl = $('#colour').val()
        brand = $('#brand').val()
        country = $('#country').val().toLowerCase();

        data = '{"query":{"filtered":{"query":{"match_all":{}},"filter":{"bool":{"must":['

        if (country) {data = data + '{"term":{"country":"' + country + '"}}'};
        if (cl) {data = data + ',{"term":{"colour":"' + cl + '"}}'};
        if (ct) {data = data + ',{"term":{"clothing_type":"' + ct + '"}}'};
        if (brand) {data = data + ',{"term":{"brand":"' + brand + '"}}'};
        data = data + ']}}}}}'
        console.log(data)

        url = 'http://localhost:9200/garments/_search'
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
                    if(r_items[r]._source.pic_title !== 'undefined') {

                    $('<img src="/static/uploads/' + r_items[r]._source.pic_title + '"; class="original">').load(function() {
                        $(this).width(150).height(150).appendTo('#images')});
                    };
                };

            }
        });
    });
});


