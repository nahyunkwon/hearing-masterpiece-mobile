 $(document).ready(function() {
                $.getJSON( "/Users/kwon/PycharmProjects/image_segmentation/plot_vector_point/instances_val2017.json", function( data ) {
                    $("#gname").html(data["file_name"]);
                    $(data["id"]).each(function(i, member) {
                        if (i != 0) { $("#members").append(", "); }
                        $("#members").append(member);
                    });
                    $.each(data["segmentation"], function(key, value) {
                        $("#albums").append("<li>" + key + ": " + value + "</li>\n");
                    });
                });
            });