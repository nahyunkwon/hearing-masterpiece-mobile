var image_json = null;

$.ajax({
    'async': false,
    'global': false,
    'url': "./img_data/artworks_2.0_metadata.json",
    'dataType': "json",
    'success': function (data) {
        image_json = data;
    }
});

var row = document.getElementById('row');

function add_image(div, src_folder, image_id, edit_url){

    var link = document.createElement('a');
    link.href = edit_url;

    var img = document.createElement('img');
    img.src = src_folder + image_id.toString() + ".jpg";

    link.appendChild(img);
    div.appendChild(link);

}

function capitalize_first_letter(str){

    return str.charAt(0).toUpperCase() + str.slice(1);
}

var username = "master";


function generate_index(image_json){

    for(var i=0;i<image_json.length;i++){

        var card = document.createElement('div');
        card.className = 'card';
        card.id = i.toString();
        row.appendChild(card);

        var inner_card = document.createElement('div');
        inner_card.className = 'inner-card';
        card.appendChild(inner_card);

        /*
        var image_index = document.createElement('div');
        image_index.className = 'image-index';
        inner_card.appendChild(image_index);
        */

        var thumbnail_wrapper = document.createElement('div');
        thumbnail_wrapper.className = 'thumbnail-wrapper';

        var edit_url = "http://ec2-3-19-255-25.us-east-2.compute.amazonaws.com///LabelMeAnnotationTool/tool.html?mode=i&collection=art_2.0&folder=art_2.0&image=" + Object.values(image_json[i])[1] + ".jpg&N=5&viewobj=e&username=" +username;
        var translate_url = "http://ec2-3-19-255-25.us-east-2.compute.amazonaws.com///LabelMeAnnotationTool/tool.html?mode=t&collection=art_2.0&folder=art_2.0&image=" + Object.values(image_json[i])[1] + ".jpg&N=5&viewobj=e&username=" +username;

        add_image(thumbnail_wrapper, "thumbnail_image/", i+1, edit_url);
        inner_card.appendChild(thumbnail_wrapper);

        var image_info = document.createElement('div');
        image_info.className = 'image-info';
        inner_card.appendChild(image_info);

        var image_info_length = Object.keys(image_json[i]).length;

        var image_info_text = "";

        for(var j=2;j<image_info_length;j++){
            if(Object.keys(image_json[i])[j] != "url"){
                var each_text = capitalize_first_letter(Object.keys(image_json[i])[j]) + ": " + Object.values(image_json[i])[j] + "<br>";
                image_info_text += each_text;
            }

        }

        image_info_text += "[<a href=\"" + edit_url + "\">Edit</a>]";

        image_info.innerHTML = image_info_text;

    }

}

generate_index(image_json);