import pandas as pd
import json


def exp(id):

    img_id = id
    image_data = json.load(open('../../public/img_data/art_filtered/art_filtered_eng/' + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    result = []
    ids = []

    for obj in ann:
        try:
            #attr_list = obj['remains'].split(',')
            color_list = obj['color'].split(',')
            loc_list = obj['color'].split(',')
            size_list = obj['color'].split(',')
            for i in range(len(attr_list)):
                if attr_list[i].strip() != "" and attr_list[i].strip() != obj['name']:


        except AttributeError:
            print('error')
            pass

    return result


def wordcloud():
    df = pd.read_csv('./expression_type.csv')
    print(df)




def main():

    id = [1, 2, 4, 5, 9, 11, 17, 18]
    final_ids = []
    final = []

    for i in id:
        final.append(exp(i))

    print(final)
    #print(len(final_ids))

    #final_result = pd.DataFrame(final, index=final_ids)

    #final_result.to_csv('./exp.csv')

    wordcloud()


if __name__ == "__main__":
    main()

