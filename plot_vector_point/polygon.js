var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 586,
    height = 640;

	var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g");


  var x = d3.scaleLinear().range([0, 586]);
	var y = d3.scaleLinear().range([640, 0]);

  x.domain([0, 586]);
  y.domain([0, 640]);

  var point = {"x": 24, "y": 31}

  var poly = [{"x":37.31, "y":373.02},
        {"x":57.4,"y":216.61},
        {"x":67.44,"y":159.21},
        {"x":77.49,"y":113.29}];

  var poly = [{"x":10, "y":10},
        {"x":500,"y":10},
        {"x":500,"y":500},
        {"x":10,"y":500}];


    svg.append('image')
    .attr('xlink:href', '000000000285.jpg')
    .attr('width', width)
    .attr('height', height)

  svg.selectAll("polygon")
    .data([poly])
  .enter().append("polygon")
    .attr("points",function(d) {
        return d.map(function(d) {
            return [x(d.x),y(d.y)].join(",");
        }).join(" ");
    });

  polygon.style("fill-opacity", .2);


