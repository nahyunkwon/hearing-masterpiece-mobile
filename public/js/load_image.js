var url_string = window.location.href;
var url = new URL(url_string);
var img_id = url.searchParams.get("img_id");
console.log(img_id);

var mode = url.searchParams.get("mode");

if(mode == "m")
    var data_location = "../image_data_preprocess/art_processed/";
else if(mode == "p")
    var data_location = "../image_data_preprocess/art_prof_processed/";

var image_data = null;
$.ajax({
    'async': false,
    'global': false,
    'url': data_location+img_id+".json",
    'dataType': "json",
    'success': function (data) {
        image_data = data;
    }
});

var img_width;
var img_height;

var img_id_list = ["1", "2", "4", "5", "9", "11", "17", "18"];
var img_size_list = [[800, 1192], [11141, 8822], [9665, 11367], [1250, 556], [4272,6000], [2880, 3579], [800, 1095], [750, 773]];

for(var i=0;i<img_id_list.length;i++){
    if(img_id_list[i] == img_id){
        img_width = img_size_list[i][0];
        img_height = img_size_list[i][1];
    }
}

console.log(image_data);