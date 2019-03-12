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
    objects_num = [];
    objects_list = []
    for(var i=annotations.length-1;i>=0;i--){
        if(objects_list.includes(annotations[i].category) == false){
            objects_list.push(annotations[i].category);
            objects_num.push("("+String(annotations[i].duplicates_num)+")");
        }
    }
    for(var i=0;i<objects_list.length;i++){
        objects_list[i] = objects_list[i]+objects_num[i];
    }
    return objects_list;
  }

function draw_polygon(seg_mode){

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
            return d.bbox.map(function(d) {
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
    return d.category+String(d.duplicates_num);})
  .on("mouseover", function(d){
            if(d.duplicates_num == 1){
                var cat = d.category;
            }
            else{
                var cat = d.category+String(d.duplicates_num);
            }

            tooltip.text(cat);
            if(voice_flag == "on"){
                responsiveVoice.cancel();
                responsiveVoice.speak(cat, "US English Male");
            }

            return tooltip.style("visibility", "visible");})
    .on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
    .on("mouseout", function(){ responsiveVoice.cancel(); return tooltip.style("visibility", "hidden");})
    .on("dblclick", function(d) {
            if(voice_flag == "on"){
                responsiveVoice.cancel();
                if(d.object_position.includes("side")){
                    voice_desc = "this is "+d.object_description +", color is "+ d.object_color +", and this is located on  the  "+ d.object_position +" of the picture";
                }
                else{
                    voice_desc = "this is "+d.object_description +", color is "+ d.object_color +", and this is located on  the  "+ d.object_position +" side of the picture";
                }
                console.log(voice_desc);
                responsiveVoice.speak(voice_desc, "US English Male");
            } });
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

//var img_id = 1;

var voice_flag = "off";

var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 800,
    height = 600;

var svg2 = d3.select(".image").append("svg")
  .attr("width", 800)
  .attr("height", 100)
  .attr("viewBox", "0 0 100 100")
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
    .attr('xlink:href', "./sample_image/"+img_file_name)
    .attr('width', this.naturalWidth)
    .attr('height', this.naturalHeight)
    .on("mouseover", function(d){
            console.log("test");
            tooltip.text("none");
            if(voice_flag == "on"){
                responsiveVoice.cancel();
                responsiveVoice.speak("none", "US English Male");
            }
            return tooltip
           .style("visibility", "visible");})
	.on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
	.on("mouseout", function(){ responsiveVoice.cancel(); return tooltip.style("visibility", "hidden");});

  var x = d3.scaleLinear().range([0, img_file.width]);
  var y = d3.scaleLinear().range([0, img_file.height]);

  x.domain([0, img_file.width]);
  y.domain([0, img_file.height]);

  draw_polygon(seg_mode);

  //svg.call(zoomListener);

var objects =  svg2.append("text")
   .attr("y", 93)//magic number here
   .attr("x", 5)
   .attr("class", "myLabel")//easy to style with CSS
   .text(objects_list.join(", "));

var data = [{label: "Voice", x: 30, y: 60 },
            {label: "Segmentation Mode", x: 130, y: 60 }];
            //{label: "Reset", x: 230, y: 60  }];

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

var buttons = svg2.selectAll('.button')
    .data(data)
  .enter()
    .append('g')
    .attr('class', 'button')
    .call(button);

function reset() {
    var t = d3.zoomIdentity.translate(0, 0).scale(1)
    svg.call(zoomListener.transform, t)
}