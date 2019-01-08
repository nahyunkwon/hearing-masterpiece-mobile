import json
import time
import matplotlib.pyplot as plt
from matplotlib.collections import PatchCollection
from matplotlib.patches import Polygon
import numpy as np
import copy
import itertools

import os
from collections import defaultdict
import sys
from pprint import pprint

'''
anns = [{'segmentation': [[216.7, 211.89, 216.16, 217.81, 215.89, 220.77, 215.89, 223.73, 217.77, 225.35, 219.12, 224.54, 219.12, 220.5, 219.66, 217.27, 219.93, 212.7, 220.46, 207.85, 219.66, 203.01, 218.85, 198.43, 217.77, 195.74, 216.7, 194.93, 215.62, 190.62, 215.62, 186.59, 214.27, 183.89, 211.85, 184.16, 211.85, 187.66, 210.24, 187.66, 209.16, 184.97, 207.81, 183.36, 205.12, 186.59, 205.12, 189.28, 201.08, 192.78, 199.74, 195.2, 196.78, 200.04, 196.51, 203.01, 198.12, 205.43, 197.32, 209.2, 196.78, 213.23, 197.05, 218.89, 199.74, 221.85, 201.62, 225.35, 201.62, 233.69, 201.08, 236.11, 202.97, 236.38, 204.85, 236.11, 204.58, 232.34, 203.78, 228.85, 205.39, 233.15, 207.81, 235.57, 208.62, 234.23, 206.74, 231.27, 205.12, 228.04, 206.74, 222.39, 208.35, 219.96, 210.77, 217.54, 211.85, 221.85, 214.54, 223.73, 212.93, 217.54, 212.93, 215.66, 215.89, 212.96, 216.16, 212.16]], 'area': 759.3375500000002, 'iscrowd': 0, 'image_id': 324158, 'bbox': [196.51, 183.36, 23.95, 53.02], 'category_id': 18, 'id': 10673}]

polygons = []

print(anns)

for ann in anns:
    for seg in ann['segmentation']:
        poly = np.array(seg).reshape((int(len(seg) / 2), 2))
        polygons.append(poly)

print(polygons)

'''


dataset = json.load(open("./plot_image_segmentation_web/instances_val2017.json", 'r'))

pprint(dataset['categories']) #data는 json 전체를 dictionary 형태로 저장하고 있음



anns, cats, imgs = {}, {}, {}
imgToAnns,catToImgs = defaultdict(list),defaultdict(list)

if 'annotations' in dataset:
    for ann in dataset['annotations']:
        imgToAnns[ann['image_id']].append(ann)
        anns[ann['id']] = ann

if 'images' in dataset:
    for img in dataset['images']:
        imgs[img['id']] = img

if 'categories' in dataset:
    for cat in dataset['categories']:
        cats[cat['id']] = cat

if 'annotations' in dataset and 'categories' in dataset:
    for ann in dataset['annotations']:
        catToImgs[ann['category_id']].append(ann['image_id'])

#pprint(dataset['images'])

