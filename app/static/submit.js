$( document ).ready(function() {

	$('#clothing_type').select2({
	allowClear: true
	});

	$('#colour').select2({
	placeholder: "Select colour",
	allowClear: true
	});

	$('#country').select2({
	allowClear: true
	});

	$('#currency').select2({
	allowClear: true
	});

    $('#images').hide();
    $('#show-picture').hide();
    $('#upload_url').parent().hide();
    $('#purchase').hide();

	console.log( "ready!" );

	$('#link').click(function(event) {
        $("#images").html("");
        event.preventDefault();
        console.log('link');
        $('#upload_url').parent().show();
    });

    $('#p_link').click(function(event) {
        event.preventDefault();
        $('#purchase').slideToggle(300);
        });

    $('#i_link').click(function(event) {
        event.preventDefault();
        $('#important').slideToggle(300);
        });

    $('#google').click(function(event) {
        $("#images").html("");
        event.preventDefault();
        console.log('google');

        ct = $('#clothing_type').val()
        cl = $('#colour').val()
        brand = $('#brand').val()
        url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBt60JNJxqV1Frk8fL-N4bHxmSJFFbirSo&cx=006641314651600601867:gkhygtjepi4&q=' + brand + ' ' + ct+ ' ' + cl +'&searchtype=image&filter=0&num=10&safe=medium'
        var results;
        $.ajax(url,  {
            async: false,
            timeout: 10000,
            success: function (data, status, jqXHR) {
            results = data;
            console.log(results)
        }});
        console.log(results)

        var r_items = [];
        for (var i=0; i<results.items.length; i++) {r_items.push(results.items[i]);
        }

        for (var r=0; r<r_items.length; r++) {
          if ( typeof r_items[r].pagemap != 'undefined' && typeof r_items[r].pagemap.cse_image != 'undefined' ) {
              $('<div class=image-container></div>').append(
              $('<a href="#"><img src="'+ r_items[r].pagemap.cse_image[0].src +'" class="original image"></a>')
              )
              .appendTo('#images')
        }}
        $('.image-container').click(function(event) {
            event.preventDefault();
            $('.image-container').css('border-color', '#9F81F7');


            $('#upload_url').val($(this).find('img').first().attr('src'));
            $(this).css('border-color', '#FFFFFF');
            $('#upload_url').parents().show();
        })

        $('#images').show();

       });

});

(function () {
    var takePicture = document.querySelector("#take-picture"),
        showPicture = document.querySelector("#show-picture");


    console.log('hide');

    if (takePicture && showPicture) {
        // Set events
        takePicture.onchange = function (event) {
            // Get a reference to the taken picture or chosen file
            var files = event.target.files,
                file;
            if (files && files.length > 0) {
                file = files[0];
                try {
                    // Get window.URL object
                    var URL = window.URL || window.webkitURL;

                    // Create ObjectURL
                    var imgURL = URL.createObjectURL(file);

                    // Set img src to ObjectURL
                    showPicture.src = imgURL;
                    $('#show-picture').show();

                    // Revoke ObjectURL
                    URL.revokeObjectURL(imgURL);
                }
                catch (e) {
                    try {
                        // Fallback if createObjectURL is not supported
                        var fileReader = new FileReader();
                        fileReader.onload = function (event) {
                            showPicture.src = event.target.result;
                            $('#show-picture').show();
                        };
                        fileReader.readAsDataURL(file);
                    }
                    catch (e) {
                        //
                        var error = document.querySelector("#error");
                        if (error) {
                            error.innerHTML = "Neither createObjectURL or FileReader are supported";
                        }
                    }
                }
            }
        };
    }
})();
