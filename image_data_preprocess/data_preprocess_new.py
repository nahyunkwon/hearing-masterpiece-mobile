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


def art_data_preprocess(img_id):
    image_data = json.load(open("./art_prof_json/" + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    i = 0
    deleted = []
    '''
    for obj in ann:
        # print(ann[i]['deleted']=="1")
        if ann[i]['deleted'] == '1':
            deleted.append(i)

        i = i + 1

    for i in deleted:
        try:
            ann.pop(i)
        except IndexError:
            print(obj, 'indexerror')

    # print(ann)
'''
    for obj in ann:
        # print(obj['polygon']['pt'])
        points = obj['polygon']['pt']

        points_list = []

        # print(type(points))

        for i in range(len(points)):
            point = []

            try:
                point.append(float(points[i]['x']))
                point.append(float(points[i]['y']))
                points_list.append(point)
            except KeyError:
                # print('keyerror', obj, len(points)) #len(points)==2
                obj['area'] = 0
                pass

        if len(points_list) != 0:
            pts_tuple = [tuple(l) for l in points_list]

            try:
                polygon = Polygon(tuple(pts_tuple))
                obj['area'] = polygon.area
            except ValueError:
                obj['area'] = 0



        # print(obj)

    sorted_ann = sorted(ann, key=lambda k: k['area'], reverse=True)

    img['object'] = sorted_ann

    with open('./art_prof_processed/' + str(img_id) + '.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


def main():
    for i in ['1','2','4','5','9','11','17','18']:

        with open("./art_prof/"+i+".xml", 'r', encoding='utf8') as f:
            xmlString = f.read()

        print("xml input (xml_to_json.xml):")
        print(xmlString)

        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

        print("\nJSON output(output.json):")
        print(jsonString)

        with open("./art_prof_json/"+i+".json", 'w', encoding='utf8') as f:
            f.write(jsonString)

    img_id = [1, 2, 4, 5, 9, 11, 17, 18]

    for i in img_id:
        art_data_preprocess(i)


    '''
    background = \
        {"name": "배경", "polygon": {{"pt": [{"x": 0, "y": 0}, {"x": img['width'], "y": 0},
                          {"x": img['width'], "y": img['height']}, {"x": 0, "y": img['height']}],
         # "category": "배경"
         "category": "background"
         }}}
    
    ann.append(background)
    '''


if __name__ == '__main__':
    main()

