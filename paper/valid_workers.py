import pandas as pd
import csv


def main():
    valid = pd.read_csv("./workers/valid_workers.csv")
    whole = pd.read_csv("./workers/whole_workers.csv")

    valid = valid['WorkerId']

    valid_list = list(valid)
    #print(valid_list)

    valid_w = []

    for i in range(len(whole)):
        #print(whole.iloc[i]['WorkerId'])
        for j in range(len(valid_list)):
            if str(whole.iloc[i]['WorkerId']) in valid_list[j]:
                valid_w.append(whole.iloc[i]['WorkerId'])
                break

    valid_w = list(dict.fromkeys(valid_w))




if __name__ == "__main__":
    main()