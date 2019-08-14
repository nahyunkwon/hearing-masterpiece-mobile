

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

var width;
var height;

function getMeta(url){
    var img = new Image();
    img.addEventListener("load", function(){
        width = this.naturalWidth;
        height = this.naturalHeight;
    });
    img.src = url;
}

console.log(image_data);