from nltk.corpus import wordnet as wn
import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon
import pandas as pd
import re

from numpy import *
import xmltodict
import pprint
import json
import requests


def attr_filter(w):
    color_terms = ["black", "white", "green", "yellow", "blue", "brown",
                   "orange", "pink", "purple", "gray", "beige", "color", "grey", "burgundy"]
    location_terms = ["right", "left", "center", "up", "above", "under", "down",
                      "corner", "bottom", "front", "rear", "side", "middle", "top", "below", "core"]
    size_terms = ["large", "small", "medium", "size"]

    if w.strip() == "red":
        return "c"
    for c in color_terms:
        if c in w:
            return "c"
    for l in location_terms:
        if l in w:
            return "l"
    for s in size_terms:
        if s in w:
            return "s"
    return "r"


def filtering(src, dest, id):
    # words = ['amazing', 'interesting', 'love', 'great', 'nice']
    '''
    words = ['clear', 'realistic', 'dark', 'female', 'outline']

    for w in words:
        tmp = wn.synsets(w)[0].pos()
        print(w, ":", tmp)
    '''
    img_id = id
    image_data = json.load(open(src + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    for obj in ann:
        try:
            attr_list = obj['attributes'].split(',')
        except AttributeError:
            pass

        color = []
        location = []
        size = []
        remains = []

        for word in attr_list:
            w = word.strip()
            result = attr_filter(w)
            if result == "c":
                color.append(w)
            elif result == "l":
                location.append(w)
            elif result == "s":
                size.append(w)
            else:
                remains.append(w)

        '''
        filtered = []
        filtered = filtered + color + location + size

        remains = list(set(attr_list)-set(filtered))
        '''
        color_str = ""
        location_str = ""
        size_str = ""
        remains_str = ""

        for i in range(len(color)):
            if i == len(color) - 1:
                color_str = color_str + color[i]
            else:
                color_str = color_str + color[i] + ", "

        for i in range(len(location)):
            if i == len(location) - 1:
                location_str = location_str + location[i]
            else:
                location_str = location_str + location[i] + ", "

        for i in range(len(size)):
            if i == len(size) - 1:
                size_str = size_str + size[i]
            else:
                size_str = size_str + size[i] + ", "

        for i in range(len(remains)):
            if i == len(remains) - 1:
                remains_str = remains_str + remains[i]
            else:
                remains_str = remains_str + remains[i] + ", "

        obj['color'] = color_str
        obj['location'] = location_str
        obj['size'] = size_str
        obj['remains'] = remains_str

    with open(dest + str(img_id) + '.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


def main():
    img_id_list = ["1", "2", "4", "5", "9", "11", "17", "18"]
    '''
    src = "../public/img_data/art_processed/"
    dest = "../public/img_data/art_filtered/art_filtered_eng/"

    for i in img_id_list:
        filtering(src, dest, i)
        '''
    color_terms = ["black", "white", "red", "green", "yellow", "blue", "brown",
                   "orange", "pink", "purple", "gray", "beige", "grey", "gold", "silver", "burgundy"]
    location_terms = ["right", "left", "center", "up", "above", "under", "down",
                      "corner", "bottom", "front", "rear", "side", "middle", "top", "below", "core", "behind", "distant"]
    size_terms = ["large", "small", "medium", "big", "narrow", "tall", "smallest", "normal", "size", "long"]

    valid = pd.read_csv('./ann_from_valid_worker.csv')

    #print(valid.loc[valid['img_id'] == 1])
    for i in img_id_list:
        valid_per = valid.loc[valid['img_id'] == int(i)]

        for j in range(len(valid_per)):
            attr_list = valid_per.iloc[j]['attributes'].split(',')
            color = []
            loc = []
            size = []
            remains = []
            for w in attr_list:
                words = w.split(' ')
                print(words)
                for s in words:
                    if s !='':
                        if s.strip() in color_terms:
                            color.append(s.strip())
                            break
                        if s.strip() in location_terms:
                            loc.append(s.strip())
                            break
                        if s.strip() in size_terms:
                            size.append(s.strip())
                            break
                        else:
                            remains.append(s.strip())


                #print(remains)

                exp = []

                no_exp = ['not', 'is', 'very', 'on']

                for r in remains:
                    #tmp = wn.synsets(r)[0].pos()
                    if r not in no_exp:
                        try:
                            tmp = wn.synsets(r)[0].pos()
                            if tmp != "n":
                                exp.append(r)
                        except IndexError:
                            pass

            valid_per.at[j, 'exp'] = str(', '.join(exp))
            valid_per.at[j, 'color'] = str(', '.join(color))
            valid_per.at[j, 'location'] = str(', '.join(loc))
            valid_per.at[j, 'size'] = str(', '.join(size))

            valid_per.at[j, 'exp_count'] = str(len(exp))
            valid_per.at[j, 'color_count'] = str(len(color))
            valid_per.at[j, 'location_count'] = str(len(loc))
            valid_per.at[j, 'size_count'] = str(len(size))

        pd.DataFrame.to_csv(valid_per, './test'+str(i)+'.csv')


def test():
    # words = ['amazing', 'interesting', 'love', 'great', 'nice']
    '''
    words = ['clear', 'realistic', 'dark', 'female', 'outline']

    for w in words:
        tmp = wn.synsets(w)[0].pos()
        print(w, ":", tmp)
    '''
    src = "../public/img_data/art_processed/"
    img_id = 2
    image_data = json.load(open(src + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    color_terms = ["black", "white", "red", "green", "yellow", "blue", "brown",
                   "orange", "pink", "purple", "gray", "beige", "color", "grey", "gold", "silver"]
    location_terms = ["right", "left", "center", "up", "above", "under", "down",
                      "corner", "bottom", "front", "rear", "side", "middle", "top", "below", "core", "behind", "distant"]
    size_terms = ["large", "small", "medium", "size", "smallest"]

    obj = ann[-1]

    if("a" == "a"):
        try:
            attr_list = obj['attributes'].split(', ')
        except AttributeError:
            pass

        color = []
        location = []
        size = []
        noun = []
        expression = []

        for w in attr_list:
            for c in color_terms:
                if c in w:
                    color.append(w)
                    break
            for l in location_terms:
                if l in w:
                    location.append(w)
                    break
            for s in size_terms:
                if s in w:
                    size.append(w)
                    break

        filtered = []
        filtered = filtered + color + location + size

        remains = list(set(attr_list)-set(filtered))

        '''

        for w in remains:
            try:
                tmp = wn.synsets(w)[0].pos()
                # print(w, ":", tmp)
                if tmp == "n":
                    # print(w)
                    noun.append(w)

                if tmp == "a" or tmp == "v" or tmp == "s":
                    expression.append(w)
            except IndexError:
                # print("indexerror")
                pass

        final = list(set(remains) - set(expression) - set(noun))
        '''

        print("original attributes list: ", attr_list)
        print()
        print("--after preprocess--")
        print("-color: ", color)
        print("-location: ", location)
        print("-size: ", size)
        print()
        print("--remains--")


if __name__ == "__main__":
    main()
