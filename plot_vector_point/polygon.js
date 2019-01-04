var margin = {top: 20, right: 20, bottom: 30, left: 50},
    width = 1000,
    height = 1000;

	var svg = d3.select("body").append("svg")
    .attr("width", width)
    .attr("height", height)
  .append("g");

  var point = {"x": 24, "y": 31}

  var poly = [{"x":37.31, "y":373.02},
        {"x":57.4,"y":216.61},
        {"x":67.44,"y":159.21},
        {"x":77.49,"y":113.29}];

  var poly = [{"x":10, "y":10},
        {"x":500,"y":10},
        {"x":500,"y":500},
        {"x":10,"y":500}];

  var list_poly = {"points": [[37.31, 373.02],
  [57.4, 216.61],
 [67.44, 159.21],
 [77.49, 113.29],
 [91.84, 86.03],
 [123.41, 84.59],
 [162.15, 96.07],
 [215.25, 86.03],
 [261.17, 70.24],
 [285.5, 68.81],
 [337.22, 68.81],
 [411.84, 93.2 ],
 [454.89, 107.55],
 [496.5, 255.35],
 [513.72, 262.53],
 [552.47, 292.66],
 [586., 324.23],
 [586., 381.63],
 [586., 449.08],
 [586., 453.38],
 [578.3 , 616.97],
 [518.03, 621.27],
 [444.84, 624.14],
 [340.09, 625.58],
 [136.32, 625.58],
 [1.43, 632.75],
 [7.17, 555.26],
 [5.74, 414.64]],
 "object": "bear",
 "width": 586,
 "height": 640}

  var img_file = '000000000285.jpg';


  var image = svg.append('image')
    .attr('xlink:href', img_file)
    .attr('width', this.naturalWidth)
    .attr('height', this.naturalHeight)

  var x = d3.scaleLinear().range([0, list_poly.width]);
  var y = d3.scaleLinear().range([0, list_poly.height]);

  x.domain([0, list_poly.width]);
  y.domain([0, list_poly.height]);


  svg.selectAll("polygon")
    .data([list_poly.points])
  .enter().append("polygon")
    .attr("points",function(d) {
        return d.map(function(d) {
            return [x(d[0]),y(d[1])].join(",");
        }).join(" ");
    });

  svg.selectAll("polygon")
  .style("fill-opacity", .5)
  //.style("stroke", "black")
  //.style("stroke-width", 5)
  .style("fill",function() {
    return "hsl(" + Math.random() * 360 + ",100%,50%)";
    });
