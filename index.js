var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 586 - margin.left - margin.right,
    height = 640 - margin.top - margin.bottom;

	var svg = d3.select("body").append("svg")
    .attr("width", width + margin.left + margin.right)
    .attr("height", height + margin.top + margin.bottom)
  .append("g")
    .attr("transform",
          "translate(" + margin.left + "," + margin.top + ")");


  var x = d3.scaleLinear().range([0, 500]);
    var y = d3.scaleLinear().range([500, 0]);

  x.domain([0, 50]);
  y.domain([0, 50]);

  var point = {"x": 24, "y": 31}

  var poly = [{"x":216.7, "y": 211.89},
        {"x":216.16,"y":217.81},
        {"x":215.89,"y":220.77},
        {"x":215.89,"y":223.73}];


  svg.selectAll("polygon")
    .data([poly])
  .enter().append("polygon")
    .attr("points",function(d) {
        return d.map(function(d) {
            return [x(d.x),y(d.y)].join(",");
        }).join(" ");
    });

  svg.append("circle")
    .attr("r", 4)
    .attr("cx", x(point.x))
    .attr("cy", y(point.y))
    .style("opacity", ".9")

svg.append("svg:image")
    .attr('x', -9)
    .attr('y', -12)
    .attr('width', 20)
    .attr('height', 24)
    .attr("xlink:href", "/Users/kwon/PycharmProjects/image_segmentation/000000000285.png")
