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
import operator


def main():
    '''
    desc = pd.read_csv("./desc/art_desc_final.csv")
    #print(desc)

    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]

    desc_list = []

    for i in range(len(desc)):
        desc['img_desc'][i] = str(desc['img_desc'][i]).replace("\n", ", ")
        desc['img_desc'][i] = str(desc['img_desc'][i]).replace("\r", "")
        desc['img_desc'][i] = str(desc['img_desc'][i]).replace(";", ", ")

    desc.to_csv("./desc/art_desc_final_2.csv")
    '''
    desc = pd.read_csv("./desc/desc_from_valid.csv")
    #print(desc)

    words = []

    selected = desc.loc[desc["img_name"] == "17.jpg"]
    selected = selected.reset_index()

    counts = []

    for i in range(len(selected)):
        wds = str(selected['img_desc'][i]).split(',')
        count = len(wds)
        counts.append(count)
        for j in wds:
            if j.strip() != '':
                words.append(j.strip().lower())
            
    print('sum')
    print(sum(counts))
    print('mean')
    print(mean(counts))
    result = dict((i, words.count(i)) for i in words)
    print(result)

    sorted_list = sorted(result.items(), key=operator.itemgetter(1), reverse=True)

    text=""

    for i in sorted_list:
        if(i[1] != 1):
            w = str(i[0])+"("+str(i[1])+"), "
        else:
            w = str(i[0])+", "

        text = text + w

    print(text)




if __name__ == "__main__":
    main()

