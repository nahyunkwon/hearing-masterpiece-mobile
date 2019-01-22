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

from pycocotools.coco import COCO
import numpy as np
import skimage.io as io
import matplotlib.pyplot as plt
import pprint

dataset = json.load(open("./plot_image_segmentation_web/instances_val2017.json", 'r'))

image_ids = [139]
'''
def get_metadata(dataset, image_ids):
    image = {}
    annotations = {}
    for i in range(0, len(image_ids)):
        for img in dataset['images']:
            if img['id'] == image_ids[i]:
                image.update(img)

        for ann in dataset['annotations']:
            if ann['image_id'] == image_ids[i]:
                annotations.update(ann)

    categories = dataset['categories']

    return image, annotations, categories


image, annotations, categories = get_metadata(dataset, image_ids)

print(image, annotations)

'''

categories = dataset['categories']

annotations = []

for img in dataset['images']:
    if img['id'] == 139:
        image = img

for ann in dataset['annotations']:
    if ann['image_id'] == 139:
        #annotations.append(ann.copy())
        seg = ann['segmentation'][0]
        ann['segmentation'] = np.array(seg).reshape((int(len(seg) / 2), 2)).tolist()

        [bbox_x, bbox_y, bbox_w, bbox_h] = ann['bbox']
        bbox_point = [[bbox_x, bbox_y], [bbox_x, bbox_y + bbox_h], [bbox_x + bbox_w, bbox_y + bbox_h],
                [bbox_x + bbox_w, bbox_y]]
        bbox = np.array(bbox_point).reshape((4, 2)).tolist()

        ann['bbox'] = bbox
        
        for cat in categories:
            if ann['category_id'] == cat['id']:
                ann['category'] = cat['name']

        for key in ['iscrowd', 'image_id', 'category_id', 'id']:
            del ann[key]

        annotations.append(ann.copy())

sorted_ann = sorted(annotations, key=lambda k: k['area'], reverse=True)

for key in ['license', 'date_captured', 'flickr_url', 'coco_url']:
    del image[key]

image['annotations'] = sorted_ann

with open('result.json', 'w') as fp:
    json.dump(image, fp, sort_keys=True, indent=1, separators=(',', ': '))
