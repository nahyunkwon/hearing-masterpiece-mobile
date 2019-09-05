import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *
import xmltodict
import pprint
import json

img_id = [1, 5, 17]

for i in img_id:
    image_data = json.load(
        open('../public/img_data/art_filtered/art_filtered_kor/' + str(i) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    result = []

    # print(ann)

    for i in range(len(ann)):
        if ann[i]['deleted'] == "0":
            result.append(ann[i])

    img['object'] = result

    with open('./test_attr/' + str(i) + '.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)
