function find_by_file_id(image_data, img_id){
    for(var i=0;i<image_data.images.length;i++){
        if(image_data.images[i].id == img_id){
            return image_data.images[i];
        }
    }
    return -1;
  }

var img_file = find_by_file_id(image_data, img_id);

var title = img_file.title;

var artist = img_file.artist;

var year = img_file.year;

var medium = img_file.medium;

var dimensions = img_file.dimensions;

var loc = img_file.location;

var desc = img_file.description;


window.onload = function() {
    document.getElementById('metadata').innerHTML = "<h2>"+title+"</h2>"
                        +"<p>"+artist+", "+year+"</p>"
                        /*
                        +"<h4>"+medium+", "+dimensions+", "+year+"</br>"
                        +artist+"</h4>"
                        +loc+"</br>"+"</br>"
                        +desc
                        */
                        ;
}


//var full_desc = title +"\n"+ artist +"\n"+ year +"\n"+ medium +"\n"+ dimensions +"\n"+ loc +"\n"+ desc;

function read_full_desc(img_id){
    var img_file = find_by_file_id(image_data, img_id);

    var desc = img_file.description;

    responsiveVoice.cancel();
    responsiveVoice.speak(desc, "US English Male");
}

function voice() {
	responsiveVoice.speak("voice enabled", "US English Male");
}

function voice_cancel(){
    responsiveVoice.cancel();
}