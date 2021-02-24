var url_string = window.location.href;
var url = new URL(url_string);
var img_id = url.searchParams.get("img_id");
var lan = url.searchParams.get("lan");

var attr_exp = url.searchParams.get("exp");
var attr_color = url.searchParams.get("color");
var attr_loc = url.searchParams.get("loc");
var attr_size = url.searchParams.get("size");
var attr_sound = url.searchParams.get("sound");
var mode = url.searchParams.get("mode");

/*
var mode = url.searchParams.get("mode");

if(mode == "m"){
    var data_location = "art_processed/";
    }
else if(mode == "p"){
    var data_location = "art_prof_processed/";
}
*/

var image_data_m = null;

$.ajax({
    'async': false,
    'global': false,
    'url': "./img_data/milano/"+String(img_id)+".json",
    'dataType': "json",
    'success': function (data) {
        image_data_m = data;
    }
});

var img_width = 1200;
var img_height = 941;



var opt = 0.55;
/*
var art_metadata_kor = null;
var art_metadata_eng = null;

$.ajax({
    'async': false,
    'global': false,
    'url': "./img_data/art_metadata/art_metadata_kor.json",
    'dataType': "json",
    'success': function (data) {
        art_metadata_kor = data;
    }
});

function metadata(id, lan) {

    if (lan == "k")
        var data = art_metadata_kor['idx'];
    else
        var data = art_metadata_eng['idx'];

    for(var i=0;i<data.length;i++){
        if(id == data['idx']){
            var metadata = data[i];
            break;
            }
    }

    document.getElementById(String(id)).innerHTML =
                        ""
                        +"<br>작가: "+metadata['작가']
                        +"<br>연도: "+metadata['연도']
                        +"<br>매체: "+metadata['매체']
                        +"<br>사조: "+metadata['사조']
                        +"<br>장르: "+metadata['장르']
                        +""
                        ;

}
*/