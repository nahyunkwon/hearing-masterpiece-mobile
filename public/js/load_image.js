

var image_data = null;
$.ajax({
    'async': false,
    'global': false,
    'url': "../image_data_preprocess/art_processed/"+img_id+".json",
    'dataType': "json",
    'success': function (data) {
        image_data = data;
    }
});

var img_width=800;
var img_height=1192;

console.log(image_data);