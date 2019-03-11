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
                        /*
                        +"<h4>"+medium+", "+dimensions+", "+year+"</br>"
                        +artist+"</h4>"
                        +loc+"</br>"+"</br>"
                        +desc
                        */
                        ;
}


//var full_desc = title +"\n"+ artist +"\n"+ year +"\n"+ medium +"\n"+ dimensions +"\n"+ loc +"\n"+ desc;

function read_full_desc(){
    responsiveVoice.cancel();
    responsiveVoice.speak("The Starry Night is an oil on canvas by the Dutch post-impressionist painter Vincent van Gogh. Painted in June 1889, it depicts the view from the east-facing window of his asylum room at Saint-Rémy-de-Provence, just before sunrise, with the addition of an idealized village. It has been in the permanent collection of the Museum of Modern Art in New York City since 1941, acquired through the Lillie P. Bliss Bequest. Regarded as among Van Gogh's finest works,The Starry Night is one of the most recognized paintings in the history of Western culture.", "US English Male");
}

function voice() {
	responsiveVoice.speak("voice enabled", "US English Male");
}

function voice_cancel(){
    responsiveVoice.cancel();
}