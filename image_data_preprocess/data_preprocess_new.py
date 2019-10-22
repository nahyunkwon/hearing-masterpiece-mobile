import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json
import requests


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


def art_data_preprocess(img_id, src, dest):
    image_data = json.load(open(src + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']
    '''
    i = 0
    deleted = []
    
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

        try:
            attr_list = obj['attributes'].split(',')

            result_attr = ""

            for i in range(len(attr_list)):
                if attr_list[i] != obj['name']:
                    if i == len(attr_list) - 1:
                        result_attr = result_attr + attr_list[i]
                    else:
                        result_attr = result_attr + attr_list[i] + ","

            obj['attributes'] = result_attr
        except AttributeError:
            pass

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

        obj['name'] = eng_to_kor(obj['name'])

        '''

        try:
            obj['attributes'] = eng_to_kor(obj['attributes'])
        except KeyError:
            pass
            '''
        try:
            obj['remains'] = eng_to_kor(obj['remains'])
        except KeyError:
            pass
        try:
            obj['color'] = eng_to_kor(obj['color'])
        except KeyError:
            pass
        try:
            obj['location'] = eng_to_kor(obj['location'])
        except KeyError:
            pass
        try:
            obj['size'] = eng_to_kor(obj['size'])
        except KeyError:
            pass

    sorted_ann = sorted(ann, key=lambda k: k['area'], reverse=True)

    img['object'] = sorted_ann

    with open(dest + str(img_id) + '.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


def whole_preprocess(img_id_list, src, dest):
    for i in img_id_list:

        with open(src+i+".xml", 'r', encoding='utf8') as f:
            xmlString = f.read()

        print("xml input (xml_to_json.xml):")
        print(xmlString)

        jsonString = json.dumps(xmltodict.parse(xmlString), indent=4, ensure_ascii=False)

        print("\nJSON output(output.json):")
        print(jsonString)

        with open(src+i+".json", 'w', encoding='utf8') as f:
            f.write(jsonString)

    for i in img_id_list:
        art_data_preprocess(i, src, dest)


def eng_to_kor(text):
    url = "https://openapi.naver.com/v1/language/translate?source=en&target=ko&text="

    client = "5KkRHJJtuSqmpyxhCLBB"
    secret = "iTYSwRMMGA"

    #request_url = "https://openapi.naver.com/v1/papago/n2mt"
    request_url = "https://openapi.naver.com/v1/language/translate"
    headers = {"X-Naver-Client-Id": client, "X-Naver-Client-Secret": secret}
    params = {"source": "en", "target": "ko", "text": text}
    response = requests.post(request_url, headers=headers, data=params)
    # print(response.text)
    result = response.json()

    return result['message']['result']['translatedText']


def main():

    src = "../public/img_data/art_filtered/art_filtered_eng/"
    dest = "../public/img_data/art_filtered/art_filtered_kor/"

    img_id_list = ["1", "2"]

    '''
    for i in img_id:
        art_data_preprocess(i, src, dest)
    '''
    #whole_preprocess(img_id_list, src, dest)
    for i in img_id_list:
        art_data_preprocess(i, src, dest)


if __name__ == '__main__':
    main()

