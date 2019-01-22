import json
import numpy as np

dataset = json.load(open("./plot_image_segmentation_web/instances_val2017.json", 'r'))

image_ids = [139, 285, 36844]


def get_metadata(dataset, image_ids):
    categories = dataset['categories']

    images = []

    for i in image_ids:
        annotations = []

        for img in dataset['images']:
            if img['id'] == i:
                image = img

        for ann in dataset['annotations']:
            if ann['image_id'] == i:
                ann_copy = ann

                seg = ann_copy['segmentation'][0]

                ann_copy['segmentation'] = np.array(seg).reshape((int(len(seg) / 2), 2)).tolist()

                [bbox_x, bbox_y, bbox_w, bbox_h] = ann_copy['bbox']
                bbox_point = [[bbox_x, bbox_y], [bbox_x, bbox_y + bbox_h], [bbox_x + bbox_w, bbox_y + bbox_h],
                              [bbox_x + bbox_w, bbox_y]]
                bbox = np.array(bbox_point).reshape((4, 2)).tolist()

                ann_copy['bbox'] = bbox

                objects = []

                for cat in categories:
                    if ann_copy['category_id'] == cat['id']:
                        ann_copy['category'] = cat['name']
                        objects.append(ann_copy['category'])

                for key in ['iscrowd', 'id']:
                    del ann_copy[key]

                annotations.append(ann_copy.copy())

        sorted_ann = sorted(annotations, key=lambda k: k['area'], reverse=True)

        image_copy = image

        for key in ['license', 'date_captured', 'flickr_url', 'coco_url']:
            del image_copy[key]


        image_copy['annotations'] = sorted_ann

        images.append(image_copy)

    total_data = {}

    total_data['images'] = images

    print(total_data)

    with open('result.json', 'w') as fp:
        json.dump(total_data, fp, sort_keys=False, indent=1, separators=(',', ': '))


get_metadata(dataset, image_ids)


