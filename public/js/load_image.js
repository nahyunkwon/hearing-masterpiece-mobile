

var image_data = null;
$.ajax({
    'async': false,
    'global': false,
    'url': "../image_data_preprocess/art_json/"+img_id+".json",
    'dataType': "json",
    'success': function (data) {
        arr = data;
    }
});

console.log(image_data);

