import pandas as pd
import json
from wordcloud import WordCloud
import matplotlib.pyplot as plt
import operator


def exp(id):
    img_id = id
    image_data = json.load(
        open('../../public/img_data/art_filtered/art_filtered_eng/' + str(img_id) + ".json", 'r', encoding='utf-8'))

    img = image_data['annotation']

    ann = img['object']

    result = []
    ids = []

    colors = []

    for obj in ann:
        try:
            color_list = obj['color'].split(',')

            for i in range(len(color_list)):
                if color_list[i].strip() != '':
                    colors.append(color_list[i].strip())

        except AttributeError:
            print('error')
            pass

    return colors


def wordcloud():
    df = pd.read_csv('./expression_type.csv')

    str_0 = ""
    str_1 = ""
    str_2 = ""
    str_3 = ""
    str_4 = ""
    str_5 = ""
    str_6 = ""

    for i in range(len(df)):
        if df.iloc[i]['type'] == 0:
            str_0 = str_0 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 1:
            str_1 = str_1 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 2:
            str_2 = str_2 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 3:
            str_3 = str_3 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 4:
            str_4 = str_4 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 5:
            str_5 = str_5 + " " + df.iloc[i]['expression']
        elif df.iloc[i]['type'] == 6:
            str_6 = str_6 + " " + df.iloc[i]['expression']

    #print(str_0)

    wordcloud = WordCloud(max_font_size=100, collocations=False, background_color="black").generate(str_6)

    fig = plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./wordcloud/color.svg')
    # plt.savefig('./wordcloud/' + 'size.svg')
    plt.show()


def color_wordcloud():

    id = [1, 2, 4, 5, 9, 11, 17, 18]
    final_ids = []
    colors = []

    for i in id:
        for j in range(len(exp(i))):
            colors.append(exp(i)[j])

    add = ['silver', 'silver', 'gold', 'gold', 'gold', 'gold', 'deep gold']

    colors = add + colors

    color_str = ""

    for i in range(len(colors)):
        color_str = color_str + " " + str(colors[i])

    print(color_str)

    wordcloud = WordCloud(max_font_size=100, collocations=False, background_color="black").generate(color_str)

    fig = plt.figure()
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.savefig('./wordcloud/color.svg')
    # plt.savefig('./wordcloud/' + 'size.svg')
    plt.show()

    #wordcloud()


def main():
    wordcloud()


if __name__ == "__main__":
    main()

