import json

def delete(img_id):
    image_data = json.load(open("./"+str(img_id)+".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    print(ann)

    ann_new = []

    for obj in ann:
        if obj['deleted'] == "0":
            ann_new.append(obj)

    print(len(ann_new))

    image_data['annotation']['object'] = ann_new

    with open(str(img_id)+".json", 'w') as fp:
        json.dump(image_data, fp, sort_keys=False, indent=1, separators=(',', ': '), ensure_ascii=False)


if __name__ == "__main__":
    id_list = [1,2,4,5,9,11,17,18]

    for i in id_list:
        delete(i)