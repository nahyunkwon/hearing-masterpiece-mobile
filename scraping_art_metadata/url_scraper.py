from selenium import webdriver
import pandas as pd
import selenium.common.exceptions


def main():

    get_url_of_artworks()
    '''

    driver.find_element_by_class_name('wiki-top-menu-search').click()

    driver.find_element_by_tag_name('input').send_keys('The Baptism of Christ Piero Della Francesca')

    driver.implicitly_wait(20)

    print(driver.find_element_by_class_name('wiki-top-menu-search-link').get_attribute('href'))
    '''


def get_url_of_artworks():

    art_df = pd.read_csv('./artworks_2.0.csv')
    #print(art_df)

    for i in range(len(art_df)):
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        # 혹은 options.add_argument("--disable-gpu")

        driver = webdriver.Chrome('./chromedriver', chrome_options=options)

        driver.get('https://www.wikiart.org/')

        search_key = art_df.iloc[i]['title'] + " " + art_df.iloc[i]['artist'].split(' ')[0]

        print(search_key)


        try:
            driver.find_element_by_class_name('wiki-top-menu-search').click()

            driver.find_element_by_tag_name('input').send_keys(search_key)

            driver.implicitly_wait(20)

            url = driver.find_element_by_class_name('wiki-top-menu-search-link').get_attribute('href')

            driver.find_element_by_tag_name('input').clear()

            print(i, url)

        except selenium.common.exceptions.ElementNotVisibleException as e:
            print(e, i)
            url = ""

        art_df.iloc[i, art_df.columns.get_loc('url')] = url

        art_df.to_csv('./artworks_2.0_url.csv')


    print(art_df)






if __name__ == "__main__":
    main()

