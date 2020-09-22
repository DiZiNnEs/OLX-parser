from typing import List

from bs4 import BeautifulSoup

from .request import Request


class PageParser:
    def __init__(self, request: Request) -> None:
        """
        constructor takes one parameter `Request`
        :param request: Request
        """
        self.request = request

    async def page_parse(self) -> List[str]:
        """
        The function parse pages
        :return: List
        """
        product = str(input('Ведите название продукта: '))
        pages_list = []
        soup = BeautifulSoup(await self.request.request(product), 'lxml')
        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                pages_list.append(pages.select_one('a')['href'] if pages.select_one('a')['href'] is not None else None)
            except TypeError as ex:
                print('`NonType` object is not subscribable')
                pass

        return pages_list

    async def page_parse_test(self, product) -> List[str]:
        """
        The function parse pages
        :return: List
        """
        pages_list = []
        soup = BeautifulSoup(await self.request.request(product), 'lxml')
        for pages in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                pages_list.append(pages.select_one('a')['href'] if pages.select_one('a')['href'] is not None else None)
            except TypeError as ex:
                print('`NonType` object is not subscribable')
                pass

        return pages_list
