import csv
from urllib import parse
import operator
import pandas as pd
import numpy as np
import re


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

    reader = csv.reader(open("./art_filtered_eng/1csv.csv"), delimiter=",")

    sortedlist = sorted(reader, key=operator.itemgetter(3), reverse=True)

    with open('./art_filtered_eng/1.csv', 'w') as out_file:
        writer = csv.writer(out_file)
        writer.writerow(('img_name', 'worker_id', 'desc'))
        writer.writerows(sortedlist)


def get_obj_list(img_id):

    img_df = pd.read_csv("./art_filtered_eng/" + img_id + "csv.csv")

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

    with open("./art_filtered_eng/obj_lists.csv", "w", newline="") as f:  # open("output.csv","wb") for Python 2
        writer = csv.writer(f)
        writer.writerows(obj_lists)


def get_stat_data(img_id):

    img_df = pd.read_csv("./art_filtered_eng/" + img_id + "csv.csv")

    new_df = pd.DataFrame.from_dict(img_df)

    new_df = new_df[['name', 'polygon/username']]

    new_df = new_df.sort_values(by=['polygon/username'])

    dups_user = new_df.pivot_table(index=['polygon/username'], aggfunc='size')

    count_list = []

    for i in range(len(dups_user)):
        count_list.append(dups_user.iloc[i])

    count_arr = np.array(count_list)

    result_list = []

    result_list.append(np.mean(count_arr))
    result_list.append(np.std(count_arr))

    return result_list


def stat_data_to_csv():

    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]

    stat_list = []

    for i in img_id:
        stat_list.append(get_stat_data(i))

    print(stat_list)

    with open("./art_filtered_eng/user_stat.csv", "w", newline="") as f:  # open("output.csv","wb") for Python 2
        writer = csv.writer(f)
        writer.writerows(stat_list)


def list_to_csv(list, dest):
    with open(dest, "w", newline="") as f:  # open("output.csv","wb") for Python 2
        writer = csv.writer(f)
        writer.writerows(list)


def join_object_data_desc():
    obj_df = pd.read_csv("../art_desc_decode/objects.csv")
    desc_df = pd.read_csv("../art_desc_decode/art_desc_2.csv")

    obj_df = obj_df.rename(columns={"workerID": "worker_id"})

    obj_df = obj_df.drop(columns=['Unnamed: 5', 'Unnamed: 6'])

    # obj_df = obj_df[['worker_id']]
    # print(obj_df)

    # desc_df = desc_df[['worker_id', 'img_desc']]

    # desc_df = desc_df.drop_duplicates(keep='last')

    # desc_df.to_csv("./art_desc_no_dup.csv", mode='w')

    # desc_df.to_csv("art_desc_no_dup.csv", mode='w')

    # obj_df = obj_df.astype(str)
    # desc_df = desc_df.astype(str)

    obj_df = obj_df.applymap(str)

    for i in range(len(obj_df)):
        obj_df.iloc[i][0] = str(obj_df.iloc[i][0]) + ".jpg"
        print(type(obj_df.iloc[i][0]))

    print(desc_df)
    # obj_df.to_csv("art_desc_no_dup.csv", mode='w')

    # join_df = obj_df.join(desc_df, lsuffix='_left', rsuffix='_right', on=['worker_id, img_name'])

    join_df = pd.merge(obj_df, desc_df, how='left', left_on=['img_name', 'worker_id'],
                       right_on=['img_name', 'worker_id'])

    join_df.to_csv("../art_desc_decode/object_info.csv", mode='w')


def desc_to_word_list(img_name):

    desc_df = pd.read_csv("../art_desc_decode/art_desc_2.csv")

    img_desc = desc_df.loc[desc_df['img_name'] == img_name]

    desc_list = []

    for i in range(len(img_desc)):
        desc_split = re.split(', |,| ; |; |;|\r|\n|and |but |with |\.', str(img_desc.iloc[i]['img_desc']))
        desc_list = desc_list + desc_split

    desc_list = list(dict.fromkeys(desc_list))

    try:
        desc_list.remove('')
    except ValueError:
        pass
    try:
        desc_list.remove('nan')
    except ValueError:
        pass
    try:
        desc_list.remove('ZCgDVLkp6')
    except ValueError:
        pass

    result_list = []
    result_list.append(img_name)
    result_list.append(desc_list)

    return result_list


def main():

    img_id = ["1", "2", "4", "5", "9", "11", "17", "18"]
    '''
    columns = ['img_id', 'art_desc']

    result = []

    for i in img_id:
        result.append(desc_to_word_list(i + ".jpg"))

    desc_df = pd.DataFrame(result, columns=columns)

    print(desc_df)

    desc_df.to_csv("./art_filtered_eng/result_desc.csv")
    '''




main()


