from typing import List

from bs4 import BeautifulSoup

from .request import Request


class HtmlHandler:
    def __init__(self, request: Request) -> None:
        """
        Constructor takes one parameter `request`
        :param request: Request
        """
        self.request = request

    async def get_pages(self, html_product: str, product_name: str) -> List[str]:
        """
        Request works here and made first request to server
        :param html_product: str
        :param product_name: str
        :return: List[str]
        """
        pages = [f'https://www.olx.kz/kokshetau/q-{product_name}']
        soup = BeautifulSoup(html_product, 'lxml')
        for html in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                page = html.select_one('a')['href']
                pages.append(page)
            except TypeError as ex:
                print('One of the objects is None')

        return pages

    async def get_urls(self, list_pages: List[str]) -> List[str]:
        """
        Request works for another links
        :param list_pages: List[str]
        :return: List[str]
        """
        html = ''
        links_of_pages = []
        for x in list_pages:
            html = await self.request.request_for_links(link=x)
            break

        soup = BeautifulSoup(html, 'lxml')

        for i in soup.select('div.offer-wrapper'):
            url = i.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']
            links_of_pages.append(url)

        return links_of_pages
