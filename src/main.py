from asyncio import run

from .browser import Browser
from .check_pages import CheckPage
from .cli import CLI
from .gui import GUI
from .html_handler import HtmlHandler
from .page_parser import PageParser
from .request import Request


async def async_main() -> None:
    """
    When executing the function, it takes the entire method from src and sends it to `runner.py`
    :return: None
    """
    user_agent = {
        'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
    }
    product_entered_by_user = str(input('Введите название продукта: '))
    request = Request(user_agent=user_agent)
    html_handler = HtmlHandler(request, product=product_entered_by_user)
    page_parser = PageParser(request)
    browser = Browser()
    cli = CLI()
    # Test
    check_pages = CheckPage(request=request, browser=browser, page_parser=page_parser, html_handler=html_handler)
    # await check_pages.check_page()
    # await check_pages.if_pages_is_exist()

    # WORK TEST CODE
    test = await check_pages.check_page(product_entered_by_user)
    print(await browser.get_html(await html_handler.html_processing()))
    if test is True:
        await check_pages.if_pages_is_exist(product_entered_by_user)
    else:
        pass
    # WORK TEST CODE
    cli.read()


    # print(await html_handler.html_processing())
    # print(await page_parser.page_parse())
    # print(await page_parser.page_parse())


def main() -> None:
    """
    Get async function from async_main() and run here
    :return:
    """
    run(async_main())
