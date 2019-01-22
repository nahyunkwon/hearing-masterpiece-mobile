import json
import numpy as np

dataset = json.load(open("./plot_image_segmentation_web/instances_val2017.json", 'r'))

image_ids = [139, 285, 18380]

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
                print(ann_copy)
                if(len(ann_copy['segmentation']) > 1):
                    seg = ann_copy['segmentation'][0]
                else:
                    seg = ann_copy['segmentation']

                seg = ann_copy['segmentation'][0]

                ann_copy['segmentation'] = np.array(seg).reshape((int(len(seg) / 2), 2)).tolist()

                [bbox_x, bbox_y, bbox_w, bbox_h] = ann_copy['bbox']
                bbox_point = [[bbox_x, bbox_y], [bbox_x, bbox_y + bbox_h], [bbox_x + bbox_w, bbox_y + bbox_h],
                              [bbox_x + bbox_w, bbox_y]]
                bbox = np.array(bbox_point).reshape((4, 2)).tolist()

                ann_copy['bbox'] = bbox

                for cat in categories:
                    if ann['category_id'] == cat['id']:
                        ann['category'] = cat['name']

                #for key in ['iscrowd', 'image_id', 'category_id', 'id']:
                 #   del ann[key]

                annotations.append(ann_copy.copy())

        sorted_ann = sorted(annotations, key=lambda k: k['area'], reverse=True)

        for key in ['license', 'date_captured', 'flickr_url', 'coco_url']:
            del image[key]

        image['annotations'] = sorted_ann

        print(image)

        images.append(image)

    print(images)

    total_data = {}

    total_data['images'] = images

    print(total_data)

    with open('result.json', 'w') as fp:
        json.dump(total_data, fp, sort_keys=False, indent=1, separators=(',', ': '))

get_metadata(dataset, image_ids)