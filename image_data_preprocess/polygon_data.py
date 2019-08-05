import csv
from urllib import parse
import operator
import pandas as pd


def txt_to_csv():

    with open('./art_description.txt', 'r') as in_file:
        stripped = (line.strip() for line in in_file)
        lines = (line.split("&") for line in stripped if line)
        l = []
        for i in lines:
            a = []
            a.append(i[0].split('=')[1])
            a.append(parse.unquote(i[1].split('=')[1]))
            a.append(parse.unquote(i[2].split('=')[1]).replace('+', ' '))
            l.append(a)
            #print(i)
        #print(l)
        with open('./art_desc.csv', 'w') as out_file:
            writer = csv.writer(out_file)
            writer.writerow(('img_name', 'worker_id', 'desc'))
            writer.writerows(l)


def sort_by_worker_id():

    reader = csv.reader(open("./art/1csv.csv"), delimiter=",")

    sortedlist = sorted(reader, key=operator.itemgetter(3), reverse=True)

    with open('./art/1.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('img_name', 'worker_id', 'desc'))
        writer.writerows(sortedlist)

def get_obj_list(img_id):

    img_df = pd.read_csv("./art/" + img_id + "csv.csv")

    new_df = pd.DataFrame.from_dict(img_df)

    new_df = new_df[['name', 'polygon/username']]

    new_df = new_df.sort_values(by=['polygon/username'])

    obj_list = []

    for i in range(len(new_df)):
        obj = new_df.iloc[i]['name']

        if obj in obj_list:
            pass
        else:
            obj_list.append(obj)
            #obj_str = obj_str+", "+obj

    print(obj_list)

    return obj_list


def obj_list_to_csv():
    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]

    obj_lists = []

    for i in img_id:
        obj_lists.append(get_obj_list(i))

    print(obj_lists)

    with open("./art/obj_lists.csv", "w", newline="") as f:  # open("output.csv","wb") for Python 2
        writer = csv.writer(f)
        writer.writerows(obj_lists)


def main():










main()


