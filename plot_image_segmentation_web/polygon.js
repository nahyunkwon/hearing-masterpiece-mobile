var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 1000,
    height = 1000;

var svg = d3.select("body").append("svg")
  .attr("width", width)
  .attr("height", height)
  .append("g");

 var img_id = 139;

 var seg_mode = "fine";

  //var anns_file = JSON.parse("./instances_val2017.json");
  //var json = require('./json_sample.json'); //(with path)

/*
  function list_reshape(list, elementsPerSubArray) {
    var matrix = [], i, k;
    for (i = 0, k = -1; i < list.length; i++) {
        if (i % elementsPerSubArray === 0) {
            k++;
            matrix[k] = [];
        }
        matrix[k].push(list[i]);
    }
    return matrix;
  }
*/

  function find_by_file_id(image_data, img_id){
    for(var i=0;i<image_data.images.length;i++){
        if(image_data.images[i].id == img_id){
            return image_data.images[i];
        }
    }
    return -1;
  }

  var img_file = find_by_file_id(image_data, img_id);
  var img_file_name = img_file.file_name;

  var tooltip = d3.select("body")
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
            return tooltip
           .style("visibility", "visible");})
	.on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
	.on("mouseout", function(){return tooltip.style("visibility", "hidden");});

  var x = d3.scaleLinear().range([0, img_file.width]);
  var y = d3.scaleLinear().range([0, img_file.height]);

  x.domain([0, img_file.width]);
  y.domain([0, img_file.height]);

  function draw_polygon(seg_mode){
    if(seg_mode == "fine"){
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("points",function(d) {
            return d.points.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }

    else{
        svg.selectAll("polygon")
        .data(img_file.annotations)
        .enter().append("polygon")
        .attr("bbox",function(d) {
            return d.bbox.map(function(d) {
                    return [x(d[0]),y(d[1])].join(","); }).join(" "); });
    }
  }

  draw_polygon(seg_mode);

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
            return tooltip.style("visibility", "visible");})
	.on("mousemove", function(){return tooltip.style("top", (event.pageY-10)+"px").style("left",(event.pageX+10)+"px");})
	.on("mouseout", function(){return tooltip.style("visibility", "hidden");});
