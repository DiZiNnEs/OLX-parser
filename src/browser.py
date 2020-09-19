from selenium import webdriver
from selenium.common import exceptions as selenium_exceptions
from bs4 import BeautifulSoup

import time


class Browser:
    def __init__(self):
        pass

    async def get_html(self, links):
        boolean_for_delete = 0
        ad_number = 1
        driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')
        for page_link in links:
            driver.get(page_link)
            try:
                driver.find_element_by_css_selector('span.button.inverted.spoiler').click()
                time.sleep(0.2)
                soup = BeautifulSoup(driver.page_source, 'lxml')
                username = soup.select_one('h4>a').get_text()
                title = soup.select_one('div.offer-titlebox>h1').get_text()
                price = soup.select_one('strong.pricelabel__value.not-arranged').get_text()
                description = soup.select_one('div.clr.lheight20.large').get_text()
                phone = soup.select_one('div.contactitem>strong').get_text()
                if boolean_for_delete == 0:
                    with open('result.txt', 'w') as file_:
                        file_.write(f'''

ОБЪЯВЛЕНИЕ НОМЕР {ad_number}
Название: {title}
Имя пользователя: {username}
Цена: {price}
Описание: {description}
Номер телефона: {phone}
Ссылка на товар: {page_link}

#-----------------------------------------------------------------------------------------------------------------------
''')
                    boolean_for_delete += 1
                else:
                    with open('result.txt', 'a') as file:
                        file.write(f'''

ОБЪЯВЛЕНИЕ НОМЕР {ad_number}
Название: {title}
Имя пользователя: {username}
Цена: {price}
Описание: {description}
Номер телефона: {phone}
Ссылка на товар: {page_link}
#-----------------------------------------------------------------------------------------------------------------------

''')

                ad_number += 1

                print(f'''
Название: {title}
Имя пользователя: {username}
Цена: {price}
Описание: {description}
Номер телефона: {phone}
Ссылка на товар: {page_link}
''')
            except KeyboardInterrupt as ex:
                print(ex)
                print('Input from user is ended')
            except selenium_exceptions.NoSuchWindowException as ex:
                print(ex)
                print('The browser was closed before the program terminated')
            except:
                pass
