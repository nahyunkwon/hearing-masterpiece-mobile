var bboxFromFeature = function(feature, zoom, width, height) {
    // Creates a bounding box around a feature's centroid,
    // based on a specified image width and height, and map zoom level
    //
    // The aim is to create a bounding box for an image requested
    // from the Mapbox Static Image API.
    var centroid = d3.geo.centroid(feature);
    var bboxBounds = geoViewport.bounds(centroid, zoom, [width, height]);
    var bboxFeature = turf.bboxPolygon(bboxBounds);

    return bboxFeature;
  };

  // Set image dimensions and zoom level
  var zoom = 17;
  var width = 960;
  var height = 350;

  var projection = d3.geo.mercator();

  var path = d3.geo.path()
    .projection(projection);

  // Create map SVG
  var svg = d3.select('.mapContainer')
    .append('svg')
    .classed('map', true)
    .attr({
      width: width,
      height: height
    });

  // Render the parcel GeoJSON outline
  d3.json('parcel.json', function(err, payload) {
    if (err) {
      throw err;
    }

    // Extract the MultiPolygon parcel feature from the FeatureCollection payload
    var parcelFeature = payload.features[0];

    // use the parcel centroid to request a static map image from the Mapbox API
    // This is the same centroid used to create the bounding box, via the geo-viewport library.
    // Therefore, I expect the result to be:
    // - a static map image that perfectly fills the SVG dimensions
    // - the parcel GeoJSON feature to perfectly align with its equivalent feature in the static image
    var centroid = d3.geo.centroid(parcelFeature);
    var publicKey = 'pk.eyJ1IjoibGFuZGNoZWNrZXIiLCJhIjoiY2lndTdibjN3MDA4dzVobTAzNGFuZmYydCJ9.vNV7sVDR2MZK3550A-LY1g';
    var staticImageUrl = 'https://api.mapbox.com/styles/v1/landchecker/cikn8jw2f00fxbgm1djbpuwxl/static/' + centroid[0] + ',' + centroid[1] + ',' + zoom + ',0.00,0.00/' + width + 'x' + height + '?access_token=' + publicKey;
    var image = '/Users/kwon/PycharmProjects/image_segmentation/000000000285.jpg'

    // Create SVG pattern for static map image,
    // and use it to fill the background rectangle
    svg.insert('defs', '.bbox')
      .append('pattern')
      .attr({
        'id': 'staticmap',
        'width': width,
        'height': height,
        'patternUnits': 'userSpaceOnUse'
      })
      .append('image')
      .attr({
        'width': width,
        'height': height,
        'xlink:href': image
      });

    // Display the background map image in an SVF rectangle that fills the SVG element.
    svg.insert('rect', '.bbox')
      .attr({
        'x': 0,
        'y': 0,
        'width': width,
        'height': height,
        'fill': 'url(#staticmap)'
      });

    // use Mapbox's geo-viewport library to compute the bounding box for the
    // static map image we'll request.
    // We want the D3 viewport to 'zoom' to the bounding box perfectly, so we
    // can overlay the parcel feature and have it line up.
    var bboxFeature = bboxFromFeature(parcelFeature, zoom, width, height);

    // BUG: The parcel's coordinates are in clockwise order, as required by D3.
    // However, if call path.bounds() on this bounding box, it returns a 1-dimensional value.
    // where every coordinate is PI (see https://github.com/mbostock/d3/issues/2796).
    // The rendering bounding box is a square, with a small inner ring artifact.
    // If I reverse the coordinates to counter-clockwise, the aspect ratio of the bounding box
    // is rendered correctly, but the parcel doesn't align. Also, the counter-clockwise ordering
    // is in opposition to the documented winding order required by D3.

    bboxFeature.geometry.coordinates[0] = bboxFeature.geometry.coordinates[0].reverse();

    // Reset the projection, then compute the scale and translation needed
    // to fit the bounding box.
    projection
      .scale(1)
      .translate([0, 0]);

    var pixelBounds = path.bounds(bboxFeature);

    console.debug('image bounding box pixel bounds, as computed by path.bounds(): ', pixelBounds);

    var xmax = pixelBounds[1][0];
    var xmin = pixelBounds[0][0];
    var ymax = pixelBounds[1][1];
    var ymin = pixelBounds[0][1];

    var scaleFactor = 1 / Math.max(
      (xmax - xmin) / width,
      (ymax - ymin) / height
    );

    var translateFactor = [
      (width - scaleFactor * (xmax + xmin)) / 2,
      (height - scaleFactor * (ymax + ymin)) / 2
    ];

    projection
      .scale(scaleFactor)
      .translate(translateFactor);

    // Render bbox on screen, for demo purposes
    // This won't be rendered in the final map, it's used to
    // scale / translate the projection to zoom the map to
    // the bounding box
    svg.append('path')
      .datum(bboxFeature)
      .attr({
        'class': 'bbox',
        'd': path
      });

    // render the parcel feature
    svg.append('path')
      .datum(parcelFeature)
      .attr({
        'class': 'parcel',
        'd': path
      });
  });