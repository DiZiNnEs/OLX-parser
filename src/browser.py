from selenium import webdriver as wd
from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup

import time
import json


class Browser:
    def __init__(self, webdriver_: webdriver):
        self.webdriver = webdriver_

    async def get_html(self, links):
        all_dates = []
        ad_number = 1
        driver = wd.Chrome('/home/dizinnes/Downloads/chromedriver')
        for page_link in links:
            driver.get(page_link)
            try:
                driver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(driver.page_source, 'lxml')

                data = {
                    "Страница": 1,
                    "Номер объявление": ad_number,
                    "Название": soup.select_one('div.offer-titlebox > h1').get_text().strip().replace('\n', ''),
                    "Имя продавца": soup.select_one('h4 > a').get_text().replace('\n', '').strip(),
                    "Цена": soup.select_one('strong.pricelabel__value.not-arranged').get_text(),
                    "Описание": soup.select_one('div.clr.lheight20.large').get_text().strip().replace('\n', ' '),
                    "Номер телефона": soup.select_one('div.contactitem > strong').get_text() + ', ',
                    "Ссылка на объявление": page_link,
                }

                all_dates.append(data)
                ad_number += 1

            except KeyboardInterrupt as ex:
                print(ex)
                print('Input from user is ended')
            except selenium_exceptions.NoSuchWindowException as ex:
                print(ex)
                print('The browser was closed before the program terminated')
            except:
                print('An error has occurred')

        dates_to_json = json.dumps(all_dates, indent=4, ensure_ascii=False)

        with open('result.json', 'w', encoding='utf8') as json_file:
            json_file.write(dates_to_json)

        return dates_to_json

    async def selenium(self, urls):
        data = {}
        results = []
        ad_number = 1
        for page in urls:
            self.webdriver.get(page)

            try:
                self.webdriver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(self.webdriver.page_source, 'lxml')
                data = {
                    "Страница": 1,
                    "Номер объявление": ad_number,
                    "Название": soup.select_one('div.offer-titlebox > h1').get_text().strip().replace('\n', ''),
                    "Имя продавца": soup.select_one('h4 > a').get_text().replace('\n', '').strip(),
                    "Цена": soup.select_one('strong.pricelabel__value.not-arranged').get_text(),
                    "Описание": soup.select_one('div.clr.lheight20.large').get_text().strip().replace('\n', ' '),
                    "Номер телефона": soup.select_one('div.contactitem > strong').get_text() + ', ',
                    "Ссылка на объявление": page,
                }
            except:
                pass

            print(data)
            results.append(data)
            ad_number += 1

        return results
