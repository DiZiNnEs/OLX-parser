from asyncio import run

from .browser import Browser
from .html_handler import HtmlHandler
from .json import Json
from .request import Request

from .cli import Cli

from .config import user_agent, driver


async def async_main() -> None:
    """
    When executing the function, it takes the entire method from src and sends it to `runner.py`
    :return: None
    """
    cli = Cli()
    cli.welcome()
    product_entered_by_user = str(input('Введите название продукта: '))

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
