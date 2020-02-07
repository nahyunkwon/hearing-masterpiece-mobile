from selenium import webdriver
import pandas as pd
import selenium.common.exceptions
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import json

def main():
    get_url_of_artworks()


def get_url_of_artworks():

    art_df = pd.read_csv('./artworks_2.0_url.csv')
    #print(art_df)

    with open('./artworks_2.0_url.json') as json_file:
        art_dict = json.load(json_file)

    for i in range(len(art_df)):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        # 혹은 options.add_argument("--disable-gpu")

        driver = webdriver.Chrome('./chromedriver', chrome_options=options)
        driver.implicitly_wait(20)

        url = art_df.iloc[i]['url']

        driver.get(url)

        # document.getElementsByClassName('dictionary-values')[1].innerText
        # document.getElementsByClassName('dictionary-values-gallery')[0].innerText
        # document.getElementsByTagName('article')[0]

        try:
            wait = WebDriverWait(driver, 10)
            list_indexes = wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, ".wiki-layout-artist-info")))

            indexes = list_indexes.find_elements_by_tag_name("li")
            print(i)
            for index in indexes:
                text = index.get_attribute("innerText")

                if "ORDER" in text:
                    break

                print(text)

                if "Original Title" in text or "Date" in text or "Style" in text or "Genre" in text\
                        or "Media" in text or "Tag" in text or "Location" in text or "Dimensions" in text\
                        or "Series" in text or "Period" in text:
                    art_dict[i][text.split(':')[0].strip()] = text.split(':')[1].strip()

            print(art_dict[i])

        except selenium.common.exceptions.ElementNotVisibleException as e:
            print(e, i)

    with open("artworks_2.0_metadata.json", "w") as json_file:
        json.dump(art_dict, json_file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()

