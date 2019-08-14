import csv
from urllib import parse


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


def sort_by_file_name():
    with open('./art_desc.csv', newline='') as csvfile:
        spamreader = csv.DictReader(csvfile, delimiter=",")
        sortedlist = sorted(spamreader, key=lambda row: (row['img_name'], row['worker_id']), reverse=False)

    with open('./sorted_art_desc.csv', 'w') as f:
        fieldnames = ['img_name', 'worker_id', 'desc']
        writer = csv.DictWriter(f, fieldnames=fieldnames)
        writer.writeheader()
        for row in sortedlist:
            writer.writerow(row)


def main():

    txt_to_csv()
    sort_by_file_name()


main()


