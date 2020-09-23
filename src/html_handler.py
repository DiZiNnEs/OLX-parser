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

    async def html_processing(self) -> List[str]:
        """
        The method returns links to the  product in the List
        :return: List[str]
        """
        product = str(input('Ведите название продукта (htmlHandler): '))  # Потом откоментируй
        links = []
        soup = BeautifulSoup(await self.request.request(product), 'lxml')
        for html in soup.select('div.offer-wrapper'):
            url = html.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']
            links.append(url)
        return links

    async def get_pages(self, html_product, product_name) -> None:
        pages = [f'https://www.olx.kz/kokshetau/q-{product_name}']
        soup = BeautifulSoup(html_product, 'lxml')
        for html in soup.select('div.pager.rel.clr>span.item.fleft'):
            try:
                page = html.select_one('a')['href']
                pages.append(page)
            except TypeError as ex:
                print('One of the objects is None')

        print(pages)