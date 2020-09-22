from .page_parser import PageParser
from .request import Request
from .browser import Browser
from .html_handler import HtmlHandler


class CheckPage:
    def __init__(self, page_parser: PageParser, request: Request, browser: Browser, html_handler: HtmlHandler):
        self.page_parser = page_parser
        self.request = request
        self.browser = browser
        self.html_handler = html_handler

    # def input_from_user(self):
    #     product = str(input('Введите название товара (CheckPage): '))
    #     return product

    async def check_page(self, product_entered_by_user):
        if len(await self.page_parser.page_parse_2(product_entered_by_user)) > 0:
            print('Ваш товар имеет больше 1 одной страницы буду её парсить')
            return True
        else:
            print('Товар имеет лишь одну страничку')
            return False

    async def if_pages_is_exist(self, product_entered_by_user):
        page = await self.page_parser.page_parse_2(product_entered_by_user)
        # request = await self.request.if_page_is_exist_requeest(str(page))
        # html_handler = await self.html_handler.html_processing2(links__=request)
        print(page)
        test = ''
        for x in page:
            test = x
        request = await self.request.if_page_is_exist_requeest(test)
        html_handler = await self.html_handler.html_processing_2(links__=request)
        test_browser = await self.browser.get_html_2(links=html_handler)
        print(test_browser)
