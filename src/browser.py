from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup

import selenium
import time


class Browser:
    def __init__(self):
        pass

    async def get_html(self, links):
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for page_link in links:
            driver.get(page_link)
            try:
                driver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                title = soup.select_one('div.offer-titlebox>h1').get_text()
                price = soup.select_one('strong.pricelabel__value.not-arranged').get_text()
                description = soup.select_one('div.clr.lheight20.large').get_text()
                phone = soup.select_one('div.contactitem>strong').get_text()
                print(f'''
Название: {title}
Цена: {price}
Описание: {description}
Номер телефона: {phone}
Ссылка на товар: {page_link}
''')
            except KeyboardInterrupt as ex:
                print(ex)
            except selenium_exceptions.NoSuchWindowException as ex:
                print('The browser was closed before the program terminated')
            except:
                pass

