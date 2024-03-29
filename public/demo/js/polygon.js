var kor = "Korean Female";
var eng = "US English Male";

var language = kor;

var username = "user_1";

var log_array = [];

var log_count = 0;

var desc_mode = 0;

function change_desc_mode(){
    if(desc_mode == 0){ //default
        return 1;
    }
    else if(desc_mode == 1){
        return 0;
    }
}

function convertArrayOfObjectsToCSV(args) {
        var result, ctr, keys, columnDelimiter, lineDelimiter, data;

        data = args.data || null;
        if (data == null || !data.length) {
            return null;
        }

        columnDelimiter = args.columnDelimiter || ',';
        lineDelimiter = args.lineDelimiter || '\n';

        keys = Object.keys(data[0]);

        result = '';
        result += keys.join(columnDelimiter);
        result += lineDelimiter;

        data.forEach(function(item) {
            ctr = 0;
            keys.forEach(function(key) {
                if (ctr > 0) result += columnDelimiter;

                result += item[key];
                ctr++;
            });
            result += lineDelimiter;
        });

        return result;
    }

function download_csv(args) {
        var data, filename, link;
        var csv = convertArrayOfObjectsToCSV({
            data: log_array
        });
        if (csv == null) return;

        filename = args || username+"_log.csv";

        if (!csv.match(/^data:text\/csv/i)) {
            csv = 'data:text/csv;charset=utf-8,' + csv;
        }
        data = encodeURI(csv);

        link = document.createElement('a');
        link.setAttribute('href', data);
        link.setAttribute('download', filename);
        link.click();
    }


function collect_log(username, point_x, point_y){
    current_log = {};
    current_log['username'] = username;
    current_log['point_x'] = event.pageX;
    current_log['point_y'] = event.pageY;

    log_array.push(current_log);
    /*
    if(log_array.length %10 == 0 && log_array.length >= 10){

        localStorage.setItem('myStorage', JSON.stringify(log_array));

        JSON.parse(localStorage.getItem('myStorage'));

    }
    */
}

function get_log_file(){
    var result = convertArrayOfObjectsToCSV(log_array);
    download_csv(result);
}

function find_by_file_id(image_data, img_id){
    for(var i=0;i<image_data.images.length;i++){
        if(image_data.images[i].id == img_id){
            return image_data.images[i];
        }
    }
    return -1;
  }

function hasNumber(myString) {
  return /\d/.test(myString);
}

function get_objects_list(annotations){
    result_list = []
    objects_list = [];

    var counts = {};

    for(var i=annotations.length-1;i>=0;i--){
        if(annotations[i].category != "배경" && annotations[i].category != "background")
            objects_list.push(annotations[i].category);
    }
    objects_list = Array.from(objects_list);
    objects_list.forEach(function(x) { counts[x] = (counts[x] || 0)+1; });

    for(var key in counts){
        result_list.push(key+"("+String(counts[key])+")");
    }

    return result_list;
  }

function draw_polygon(seg_mode){

    if(seg_mode == "fine"){ //fine(polygon mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("points", function(d) {
            return d.segmentation.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); })
        ;
    }

    else if(seg_mode == "rough"){ //rough(bbox mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("points",function(d) {
            return d.bbox.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }

    //polygon opacity, fill color(random)
  svg.selectAll("polygon")
  .style("fill-opacity", .000001)
  //.style("stroke", "black")
  //.style("stroke-width", 5)

  .attr("category", function(d){
    return d.category+String(d.duplicates_num);})
    .append("svg:title")
    .text(function(d) {

        if(d.category == "background"){
            if(d.objects_color == undefined && d.object_position == undefined)
                return d.category + ".." + "";
            else
                return d.category + ".." + d.object_description +" . painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            }

        else{
            if(d.duplicates_num != 1)
                return d.category + ".." + d.object_description +" . painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            else
                return d.category + ".." + d.object_description +" . painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            }
     });
}

function draw_polygon_by_button(seg_mode, cat){

    var selected_list = [];

    for(var i=0;i<img_file.annotations.length;i++){
        if(img_file.annotations[i].category == cat || img_file.annotations[i].category == "배경"){
            selected_list.push(img_file.annotations[i]);
        }
    }

    if(seg_mode == "fine"){ //fine(polygon mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(selected_list)
        .enter().append("polygon")
        .attr("points", function(d) {
            return d.segmentation.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); })
        ;
    }

    else if(seg_mode == "rough"){ //rough(bbox mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(selected_list)
        .enter().append("polygon")
        .attr("points",function(d) {
            return d.bbox.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }

    //polygon opacity, fill color(random)
  svg.selectAll("polygon")
  .style("fill-opacity", .000001)
  .attr("category", function(d){
    return d.category+String(d.duplicates_num);})
    .append("svg:title")
    .text(function(d) {

        if(d.category == "background"){
            if(d.objects_color == undefined && d.object_position == undefined)
                return d.category + "..";
            else
                return d.category + ".." + d.object_description +" . painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            }

        else{
            if(d.duplicates_num != 1)
                return d.category  + ".." + d.object_description +" . painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            else
                return d.category + ".." + d.object_description +" .  painted "+ d.object_color +", located at "+ d.object_position +" side of the painting";
            }
            });
}

function change_voice_option(voice_flag){
    if(voice_flag == "on")
        return "off";
    else if(voice_flag == "off")
        return "on";
}

function voice(voice_flag) {
	voice_flag = change_voice_option(voice_flag);
	if(voice_flag == "on")
	    responsiveVoice.speak("voice enabled", language);
	else
	    responsiveVoice.speak("voice disabled", language);
	return voice_flag;
}

function change_seg_mode(seg_mode){
    if(seg_mode == "fine")
        return "rough";
    else if(seg_mode == "rough")
        return "fine";
}

var voice_flag = "on";

var margin = {top: 0, right: 20, bottom: 0, left: 50},
    width = 800,
    height = 900;

var svg2 = d3.select(".image").append("svg")
  .attr("width", 800)
  .attr("height", 10)
  .attr("viewBox", "0 55 10 50")
  .attr("preserveAspectRatio", "xMinYMin meet")
  .append("g");

var svg = d3.select(".image").append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", "0 0 800 500")
  .attr("preserveAspectRatio", "xMinYMin meet")
  .append("g");

svg.append("rect")
    .attr("width", "100%")
    .attr("height", "100%")
    .attr("fill", "white");


 var seg_mode = "fine";

  var img_file = find_by_file_id(image_data, img_id);
  var img_file_name = img_file.file_name;

  var objects_list = get_objects_list(img_file.annotations);

  var sorted_by_point = img_file.sorted_by_point;

  var sorted_count=0;

  var tooltip = d3.select(".image")
	.append("div")
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.style("background", "white");

var zoomListener = d3.zoom()
    .scaleExtent([1, 5])
    .on("zoom", zoomed)

function zoomed() {
    if (d3.event.transform.k === 1) d3.event.transform.y = 0;
    if (d3.event.transform.x > 0) d3.event.transform.x = 0;
    svg.attr("transform", d3.event.transform);
    x.call(d3.event.transform.rescaleX(x));
    y.call(d3.event.transform.rescaleY(y));
}

var rect = d3.select('body').append("rect")
    .attr("x", 0)
    .attr("y", 0)
    .attr("width", 500)
    .attr("height", 500)
    .style("fill", "#ccc")
    .style("fill-opacity", ".3")
    .style("stroke", "#666")
    .style("stroke-width", "1.5px");

  var image = svg.append('image')
    .attr('xlink:href', "https://github.com/KwonNH/image_seg_viewer_interface/blob/master/public/sample_image/"+img_file_name+"?raw=true")
    .attr("x", 1)
    .attr("y", 1)
    .attr('width', img_file.width)
    .attr('height', img_file.height);

  var x = d3.scaleLinear().range([0, img_file.width]);
  var y = d3.scaleLinear().range([0, img_file.height]);

  x.domain([0, img_file.width]);
  y.domain([0, img_file.height]);

  draw_polygon(seg_mode);

  //svg.call(zoomListener);

/*
var objects =  svg2.append("text")
   .attr("y", 93)//magic number here
   .attr("x", 5)
   .attr("class", "object_list")//easy to style with CSS
   .data([objects_list])
   .text(function(d){
    return(d);
   })
   .on("click", function(d){console.log(d);});
*/
var data = //[{label: "상세설명모드", x: parseInt(img_file.width)+70, y: 30 },
            [{label: "Segmentation Mode", x: 70, y:  parseInt(img_file.height)+70}];
            //{label: "Reset", x: 230, y: 60  }];
/*
var button = d3.button()
    .on('press', function(d, i) {
        if(d.label == "Voice"){
            voice_flag = voice(voice_flag);
        }
        else if(d.label == "Segmentation Mode"){
            seg_mode = change_seg_mode(seg_mode);
            draw_polygon(seg_mode);
        }
        else if(d.label == "Reset"){
            reset();
            this.release();
        }
        else if(d.label == "상세설명모드"){

            svg.selectAll("svg:title").remove();

            desc_mode = change_desc_mode();
            draw_polygon();
        }
    })
    .on('release', function(d, i) {
        if(d.label == "Voice"){
            voice_flag = voice(voice_flag);
        }
        else if(d.label == "Segmentation Mode"){
            seg_mode = change_seg_mode(seg_mode);
            draw_polygon(seg_mode);
        }
        else if(d.label == "상세설명모드"){

            desc_mode = change_desc_mode();
            draw_polygon();

        }
    });

var buttons = svg.selectAll('.button')
    .data(data)
  .enter()
    .append('g')
    .attr('class', 'button')
    .call(button);
    */
/*
function reset() {
    var t = d3.zoomIdentity.translate(0, 0).scale(1)
    svg.call(zoomListener.transform, t)
}

function doc_keyUp(e) {
    if (e.ctrlKey && e.keyCode == 86) { //enable voice (ctrl+v)
        voice_flag = voice(voice_flag);
    }
    else if(e.ctrlKey && e.keyCode == 83){ //change seg mode (ctrl+s)
        seg_mode = change_seg_mode(seg_mode);
        draw_polygon(seg_mode);
    }
    else if(e.ctrlKey && e.keyCode == 68){ //download log file (ctrl+d)
        get_log_file();
    }
    else if(e.keyCode == 39){
        if(sorted_count < sorted_by_point.length-1){
            sorted_count++;
            responsiveVoice.speak(sorted_by_point[sorted_count], language);
        }
        else{
            responsiveVoice.speak(sorted_by_point[sorted_by_point.length-1], language);
        }
    }
    else if(e.keyCode == 37){
        if(sorted_count > 0){
            sorted_count--;
            responsiveVoice.speak(sorted_by_point[sorted_count], language);
        }
        else{
            responsiveVoice.speak(sorted_by_point[0], language);
        }
    }
}
// register the handler
document.addEventListener('keyup', doc_keyUp, false);
*/

function seg_mode_button(seg_mode){
     seg_mode = change_seg_mode(seg_mode);
     draw_polygon(seg_mode);

     return seg_mode;
}


var arrayToModify = [];
window.onload = function () {
    var i, buttonsToCreate, buttonContainer, newButton;

    buttonsToCreate = objects_list;
    buttonContainer = document.getElementById('buttons2');

    for (i = 0; i < buttonsToCreate.length; i++) {

      newButton = document.createElement('input');
      newButton.type = 'button';
      newButton.value = buttonsToCreate[i];
      newButton.id = buttonsToCreate[i];

      newButton.onclick = function () {
        var cat = String(this.id).split("(")[0];
        draw_polygon_by_button(seg_mode, cat);
      };
      buttonContainer.appendChild(newButton);
    }

    document.getElementById('metadata').innerHTML =
                        "<div class=\"metadata\">"
                        +"<h2>"+title+"</h2>"
                        +"<p>"+artist+", "+year+"</p>"
                        +"</div>"
                        /*
                        +"<h4>"+medium+", "+dimensions+", "+year+"</br>"
                        +artist+"</h4>"
                        +loc+"</br>"+"</br>"
                        +desc
                        */
                        ;
};

var lastTouchEnd = 0;
document.documentElement.addEventListener('touchend', function (event) {
    var now = (new Date()).getTime();
    if (now - lastTouchEnd <= 300) {
      event.preventDefault();
    }
    lastTouchEnd = now;
}, false);

function objects_list_to_string(objects_list){
    return String(objects_list);
}