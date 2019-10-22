import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json
import requests
import csv
import pandas as pd
import statistics as st
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from nltk.corpus import wordnet as wn
import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json
import requests


def get_stat_data():
    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]

    average_list = []
    stdev_list = []
    len_list = []

    for id in img_id:
        img_df = pd.read_csv("./original_data/" + id + ".csv")

        new_df = pd.DataFrame.from_dict(img_df)
        deleted = new_df[new_df['object__deleted'] == 0]
        # print(deleted['object__polygon__username'])

        dups = deleted.pivot_table(index=['object__polygon__username'], aggfunc='size')
        # print(len(deleted))

        dups_list = []
        for i in range(len(dups)):
            dups_list.append(dups[i])

        len_list.append(len(dups_list))
        average_list.append(sum(dups_list) / float(len(dups_list)))
        stdev_list.append(st.stdev(dups_list))

    print(average_list)
    print(stdev_list)

    final = pd.DataFrame(list(zip(img_id, len_list, average_list, stdev_list)),
                         columns=['img_id', 'count', 'average', 'stdev'])
    print(final)

    # final.to_csv("./valid_stat.csv", mode='w')


def attributes_analysis(id):
    image_data = json.load(open('./valid_eng/' + str(id) + ".json", 'r', encoding='utf-8'))
    img = image_data['annotation']

    ann = img['object']

    remains = []
    color = []
    size = []
    location = []

    for obj in ann:
        if obj['deleted'] == "0":
            # print(obj['deleted'])
            if obj['remains'] != "":
                obj_remains = obj['remains'].split(',')
                obj_remains = list(map(lambda x: x.strip(), obj_remains))

                remains = remains + obj_remains

            if obj['color'] != "":
                obj_color = obj['color'].split(',')
                obj_color = list(map(lambda x: x.strip(), obj_color))

                color = color + obj_color

            if obj['size'] != "":
                obj_size = obj['size'].split(',')
                obj_size = list(map(lambda x: x.strip(), obj_size))

                size = size + obj_size

            if obj['location'] != "":
                obj_location = obj['location'].split(',')
                obj_location = list(map(lambda x: x.strip(), obj_location))

                location = location + obj_location
    '''
    print(remains)
    print(color)
    print(size)
    print(location)
    '''
    all_count = []
    #all_count.append(id)
    all_count.append(len(remains))
    all_count.append(len(color))
    all_count.append(len(size))
    all_count.append(len(location))

    remains_text = ""
    for i in range(len(remains)):
        remains_text = remains_text + " " + remains[i]

    color_text = ""
    for i in range(len(color)):
        color_text = color_text + " " + color[i]

    location_text = ""
    for i in range(len(location)):
        location_text = location_text + " " + location[i]

    size_text = ""
    for i in range(len(size)):
        size_text = size_text + " " + size[i]

    #print(size_text)


    final = remains_text + " " + color_text  + " " +  location_text  + " " + size_text

    final = final.replace("  ", " ")
    final = final.replace("_", "")
    final = final.replace(".", "")
    #print(final)
    '''

    remains_text = remains_text.replace("  ", " ")
    remains_text = remains_text.replace("_", "")
    remains_text = remains_text.replace(".", "")

    color_text = color_text.replace("  ", " ")
    color_text = color_text.replace("_", "")
    color_text = color_text.replace(".", "")

    location_text = location_text.replace("  ", " ")
    location_text = location_text.replace("_", "")
    location_text = location_text.replace(".", "")

    size_text = size_text.replace("  ", " ")
    size_text = size_text.replace("_", "")
    size_text = size_text.replace(".", "")
    '''

    return remains_text, color_text, location_text, size_text
    #return all_count

    #return final


def main():

    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]

    exp = []
    color = []
    size = []
    location = []

    color_terms = ["black", "white", "red", "green", "yellow", "blue", "brown",
                   "orange", "pink", "purple", "gray", "beige", "grey", "gold", "silver"]
    location_terms = ["right", "left", "center", "up", "above", "under", "down",
                      "corner", "bottom", "front", "rear", "side", "middle", "top", "below", "core", "behind"]
    size_terms = ["large", "small", "medium", "big", "narrow", "tall", "smallest", "normal", "size"]
    '''

    id = 17
    text = attributes_analysis(id)

    '''

    text = ""
    for id in img_id:
        text = text + " "+ attributes_analysis(id)[2]

    words = text.split(" ")
    #print(text)

    final_text = ""

    for i in range(len(words)):
        if words[i].strip() in location_terms:
            final_text = final_text + " " + words[i].strip()
        '''
        w = words[i].strip()
        try:
            tmp = wn.synsets(w)[0].pos()
            if tmp != "n" and w != "long" and w != "distant":
                final_text = final_text + " " + w
        except IndexError:
            pass
        # print(w, ":", tmp)
        '''

    print(final_text)

    #final_text = final_text + " smallest smallest normal normal normal narrow tall size size size size size size size size size size size long long long long long long long long long long"
    final_text = final_text + " distant distant distant distant distant distant distant distant distant"

    wordcloud = WordCloud(max_font_size=100, collocations=False, background_color="black").generate(final_text)

    fig = plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./wordcloud/' + str(id) + '.svg')
    #plt.savefig('./wordcloud/' + 'size.svg')
    plt.show()
    '''
    
    for i in img_id:
        count = attributes_analysis(i)
        
        exp.append(count[0])
        color.append(count[1])
        size.append(count[2])
        location.append(count[3])
        

    final = pd.DataFrame(list(zip(img_id, exp, color, location, size)),
                         columns=['img_id', 'expression', 'color', 'location', 'size'])

    print(final)

    final.to_csv("./attributes_stat.csv", mode='w')
    '''

if __name__ == '__main__':
    main()

