import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

import numpy as np
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
    desc = pd.read_csv("./desc/art_desc_final_2.csv")
    # print(desc)

    counts = []
    sum = 0

    #selected = desc.loc[desc["img_name"] == "18.jpg"]
    #selected = selected.reset_index()

    for i in range(len(desc)):
        counts.append(len(str(desc['img_desc'][i]).split(',')))

    print(np.mean(counts), np.std(counts))


if __name__ == "__main__":
    main()

