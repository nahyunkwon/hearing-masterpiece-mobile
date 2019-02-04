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

window.onload = function() {
    document.getElementById('metadata').innerHTML = "<h3>"+title+"</h3>"+
                        artist+", "+year+"</br>"
                        ;
}
