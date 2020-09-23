from asyncio import run
from selenium import webdriver

from .browser import Browser
from .html_handler import HtmlHandler
from .json import Json
from .request import Request


async def async_main() -> None:
    """
    When executing the function, it takes the entire method from src and sends it to `runner.py`
    :return: None
    """
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    driver = webdriver.Chrome('/home/dizinnes/Downloads/chromedriver')

    product_entered_by_user = 'квартира'  # str(input('Введите название продукта: '))

    request = Request(user_agent=user_agent, product_name=product_entered_by_user)
    html_handler = HtmlHandler(request=request)
    html = await request.request()
    browser = Browser(webdriver_=driver)
    json = Json(browser=browser)

    links_to_pages = await html_handler.get_pages(html_product=html, product_name=product_entered_by_user)
    links_to_url = await html_handler.get_urls(list_pages=links_to_pages)
    browser = await browser.selenium(urls=links_to_url)

    json.add(browser)
    json.read()


def main() -> None:
    """
    Get async function from async_main() and run here
    :return:
    """
    run(async_main())
