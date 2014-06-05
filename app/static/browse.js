ct = $('#clothing_type').val()
cl = $('#colour').val()
brand = $('#brand').val()
url = 'https://www.googleapis.com/customsearch/v1?key=AIzaSyBt60JNJxqV1Frk8fL-N4bHxmSJFFbirSo&cx=006641314651600601867:gkhygtjepi4&q=' + brand + ' ' + ct+ ' ' + cl +'&searchtype=image&filter=0&num=10&safe=medium'
var results;
$.ajax(url, {success: function (data, status, jqXHR) {
    results = data;
}});

var r_items = [];
for (var i=0; i<results.items.length; i++) {r_items.push(results.items[i])}

for (var r=0; r<r_items.length; r++) {$('<img src="'+ r_items[r].pagemap.cse_image[0].src +'" class="original">').load(function() {
  $(this).width(150).height(150).appendTo('#images');
})}