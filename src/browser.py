from typing import (
    List,
    Dict,
    Union,
    Any
)

from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup

import time


class Browser:
    def __init__(self, webdriver_: webdriver) -> None:
        self.webdriver = webdriver_

    async def selenium(self, urls: List[str]) -> List[Dict[str, Union[int, Any]]]:
        results = []
        ad_number = 1
        for page in urls:
            self.webdriver.get(page)
            try:
                self.webdriver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(self.webdriver.page_source, 'lxml')
                data = {
                    "Номер объявление": ad_number,
                    "Название": soup.select_one('div.offer-titlebox > h1').get_text().strip().replace('\n', ''),
                    "Имя продавца": soup.select_one('h4 > a').get_text().replace('\n', '').strip(),
                    "Цена": soup.select_one('strong.pricelabel__value.not-arranged').get_text(),
                    "Описание": soup.select_one('div.clr.lheight20.large').get_text().strip().replace('\n', ' '),
                    "Номер телефона": soup.select_one('div.contactitem > strong').get_text() + ', ',
                    "Ссылка на объявление": page,
                }
                results.append(data)
            except AttributeError as ex:
                print('Какой-то атрибут не поддерживает `get_text`')
                print(ex)
            except selenium_exceptions.NoSuchElementException as ex:
                print('Какой-то из элементов не сущетсвует или преждевременно закрыли браузер')
                print(ex)
            ad_number += 1
        return results
