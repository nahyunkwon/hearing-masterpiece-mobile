import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json
import requests

def to_json():
    with open("./2.xml", 'r', encoding='utf8') as f:
        xmlString = f.read()

    print("xml input (xml_to_json.xml):")
    print(xmlString)

    jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

    print("\nJSON output(output.json):")
    print(jsonString)

    with open("./2.json", 'w', encoding='utf8') as f:
        f.write(jsonString)


def preprocess(src, dest, img_id):
    image_data = json.load(open(src + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

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

    sorted_ann = sorted(ann, key=lambda k: k['area'], reverse=True)

    occluded = []
    not_occluded = []

    for i in range(len(sorted_ann)):
        if sorted_ann[i]['occluded'] == "yes":
            occluded.append(sorted_ann[i])
        else:
            not_occluded.append(sorted_ann[i])

    final_ann = occluded + not_occluded

    not_deleted_ann = []

    for i in range(len(final_ann)):
        if final_ann[i]['deleted'] == "0":
            not_deleted_ann.append(final_ann[i])

    img['object'] = not_deleted_ann

    with open(dest + str(img_id) + '_2.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)

def filterTheDict(dictObj, callback):
    newDict = dict()
    # Iterate over all the items in dictionary
    for (key, value) in dictObj.items():
        # Check if item satisfies the given condition then add to new dict
        if callback((key, value)):
            newDict[key] = value
    return newDict


def main():
    preprocess("./", "./", 2)






if __name__ == "__main__":
    main()