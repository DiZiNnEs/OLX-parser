from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup

import time
import json
import os.path


class Browser:
    def __init__(self):
        pass

    async def get_html(self, links):
        all_dates = []
        ad_number = 1
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for page_link in links:
            driver.get(page_link)
            try:
                driver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(driver.page_source, 'lxml')

                data = {
                    "ad_number": ad_number,
                    "title": soup.select_one('div.offer-titlebox > h1').get_text(),
                    "username": soup.select_one('h4 > a').get_text(),
                    "price": soup.select_one('strong.pricelabel__value.not-arranged').get_text(),
                    "description": soup.select_one('div.clr.lheight20.large').get_text(),
                    "phone_number": soup.select_one('div.contactitem > strong').get_text(),
                    "link_to_page": page_link,
                }

                all_dates.append(data)

                json_str = json.dumps(data, indent=4)
                with open('result.json', 'w', encoding='utf8') as json_file:
                    json_file.write(json_str)

                ad_number += 1
            except KeyboardInterrupt as ex:
                print(ex)
                print('Input from user is ended')
            except selenium_exceptions.NoSuchWindowException as ex:
                print(ex)
                print('The browser was closed before the program terminated')
            except:
                pass

        json_test = json.dumps(all_dates, indent=4)

        with open('result.json', 'w', encoding='utf8') as json_file:
            json_file.write(json_test)
