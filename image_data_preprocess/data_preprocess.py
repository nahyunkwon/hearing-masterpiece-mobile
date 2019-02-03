import json
import numpy as np
from matplotlib.patches import Polygon
from shapely.geometry import Polygon

from numpy import *


def main():
    image_data = json.load(open("./image_data.json", 'r'))

    images = image_data['images']
    for img in images:
        ann = img['annotations']

        for obj in ann:
            obj_list = obj['segmentation']

            x_points = []
            y_points = []

            for i in obj_list:
                i[0] = float(i[0])
                i[1] = float(i[1])

                x_points.append(i[0])
                y_points.append(i[1])

            obj_tuple = [tuple(l) for l in obj_list]

            polygon = Polygon(tuple(obj_tuple))

            obj['area'] = polygon.area

            bbox_point = [[min(x_points), min(y_points)], [max(x_points), min(y_points)], [max(x_points), max(y_points)]
                          , [min(x_points), max(y_points)]]
            bbox = np.array(bbox_point).reshape((4, 2)).tolist()

            obj['bbox'] = bbox

    with open('result.json', 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


if __name__ == '__main__':
    main()

