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
    objects_list = []
    for(var i=0;i<annotations.length;i++){
        if(hasNumber(annotations[i].category) == false){
            objects_list.push(annotations[i].category);
            }
    }
    return objects_list;
  }

function draw_polygon(seg_mode){
  var x = d3.scaleLinear().range([0, img_file.width]);
  var y = d3.scaleLinear().range([0, img_file.height]);

  x.domain([0, img_file.width]);
  y.domain([0, img_file.height]);

    if(seg_mode == "fine"){ //fine(polygon mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("points",function(d) {
            return d.segmentation.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }

    else if(seg_mode == "rough"){ //rough(bbox mode)
        d3.selectAll("polygon").remove();
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("points",function(d) {
            return d.bbox.map(function(d) {console.log("here");
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }

    //polygon opacity, fill color(random)
  svg.selectAll("polygon")
  .style("fill-opacity", .5)
  //.style("stroke", "black")
  //.style("stroke-width", 5)
  .style("fill",function() {
    return "hsl(" + Math.random() * 360 + ",100%,50%)";
  })
  .attr("category", function(d){
    return d.category;})
  .on("mouseover", function(d){
            tooltip.text(d.category);
            if(voice_flag == "on"){
                responsiveVoice.cancel();
                responsiveVoice.speak(d.category, "US English Male");
            }
            //speachSynthesis.stop();
            //speechSynthesis.speak(new SpeechSynthesisUtterance(d.category));
            return tooltip.style("visibility", "visible");})
    .on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
    .on("mouseout", function(){return tooltip.style("visibility", "hidden");});

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
	    responsiveVoice.speak("voice enabled", "US English Male");
	else
	    responsiveVoice.speak("voice disabled", "US English Male");
	return voice_flag;
}

function change_seg_mode(seg_mode){
    if(seg_mode == "fine")
        return "rough";
    else if(seg_mode == "rough")
        return "fine";
}

var voice_flag = "off";

var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 1000,
    height = 1000;

var svg = d3.select("#image").append("svg")
  .attr("width", width)
  .attr("height", height)
  .attr("viewBox", "0 0 1000 1000")
  .attr("preserveAspectRatio", "xMinYMin meet")
  .append("g");

 var img_id = 139;

 var seg_mode = "fine";

  var img_file = find_by_file_id(image_data, img_id);
  var img_file_name = img_file.file_name;

  var objects_list = get_objects_list(img_file.annotations);

  var tooltip = d3.select("#image")
	.append("div")
	.style("position", "absolute")
	.style("z-index", "10")
	.style("visibility", "hidden")
	.style("background", "white");

  var image = svg.append('image')
    .attr('xlink:href', "./sample_image/"+img_file_name)
    .attr('width', this.naturalWidth)
    .attr('height', this.naturalHeight)
    .on("mouseover", function(d){
            tooltip.text("none");
            if(voice_flag == "on"){
                responsiveVoice.cancel();
                responsiveVoice.speak("none", "US English Male");
            }
            return tooltip
           .style("visibility", "visible");})
	.on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
	.on("mouseout", function(){return tooltip.style("visibility", "hidden");});

  draw_polygon(seg_mode);

var objects =  svg.append("text")
   .attr("y", img_file.height+15)//magic number here
   .attr("x", 0)
   .attr("class", "myLabel")//easy to style with CSS
   .text(objects_list.join(", "));

var data = [{label: "Voice", x: img_file.width/20, y: img_file.height+50 },
            {label: "Segmentation Mode", x: img_file.width/20+100, y: img_file.height+50 }];

var button = d3.button()
    .on('press', function(d, i) {
        if(d.label == "Voice"){
            voice_flag = voice(voice_flag);
        }
        else if(d.label == "Segmentation Mode"){
            seg_mode = change_seg_mode(seg_mode);
            draw_polygon(seg_mode);
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
    });

var buttons = svg.selectAll('.button')
    .data(data)
  .enter()
    .append('g')
    .attr('class', 'button')
    .call(button);

