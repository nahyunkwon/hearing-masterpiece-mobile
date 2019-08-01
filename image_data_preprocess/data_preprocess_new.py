import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json


def xml_to_json(img_id):
    with open("./image_data/"+str(img_id)+".xml", 'r', encoding='utf-8') as f:
        xml_string = f.read()

    print("xml input (xml_to_json.xml):")
    print(xml_string)

    json_string = json.dumps(xmltodict.parse(xml_string), indent=4, ensure_ascii=False)

    print("\nJSON output(output.json):")
    print(json_string)

    with open("./image_data/"+str(img_id)+".json", 'w', encoding='utf-8') as f:
        f.write(json_string)


def main():

    img_id = 1
    xml_to_json(img_id)

    image_data = json.load(open("./image_data/"+str(img_id)+".json", 'r', encoding='utf-8'))

    images = image_data['annotation']
    for img in images:
        ann = img['object']

        background = \
            {"name": "배경", "polygon": {{"pt": [{"x": 0, "y": 0}, {"x": img['width'], "y": 0},
                              {"x": img['width'], "y": img['height']}, {"x": 0, "y": img['height']}],
             # "category": "배경"
             "category": "background"
             }}}

        ann.append(background)

        for obj in ann:
            obj_list = obj['segmentation']

            x_points = []
            y_points = []

            # calculate area
            for i in obj_list:
                i[0] = float(i[0])
                i[1] = float(i[1])

                x_points.append(i[0])
                y_points.append(i[1])

            obj_tuple = [tuple(l) for l in obj_list]

            polygon = Polygon(tuple(obj_tuple))

            obj['area'] = polygon.area

            # calculate bbox
            bbox_point = [[min(x_points), min(y_points)], [max(x_points), min(y_points)], [max(x_points), max(y_points)]
                          , [min(x_points), max(y_points)]]
            bbox = np.array(bbox_point).reshape((4, 2)).tolist()

            obj['bbox'] = bbox

        sorted_by_point = sorted(ann, key=lambda k: [k['bbox'][0][1], k['bbox'][0][0]])

        # calculate duplicates
        objects = []

        object_counted = []

        for i in sorted_by_point:
            objects.append(i['category'])
            object_count = objects.count(i['category'])

            object_counted.append(object_count)

        count = 0

        for i in sorted_by_point:
            i['duplicates_num'] = object_counted[count]
            count = count + 1

        # getting category list
        cat_list = []

        for i in sorted_by_point:
            if i['duplicates_num'] != 1:
                cat_list.append(i['category']+str(i['duplicates_num']))
            else:
                cat_list.append(i['category'])

        sorted_ann = sorted(sorted_by_point, key=lambda k: k['area'], reverse=True)

        img['sorted_by_point'] = cat_list

        img['annotations'] = sorted_ann

    with open('result_eng.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    main()

