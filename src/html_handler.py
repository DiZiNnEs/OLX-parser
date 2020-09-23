from typing import List

from bs4 import BeautifulSoup

from .request import Request


class HtmlHandler:
    def __init__(self, request: Request, product: str) -> None:
        """
        Constructor takes one parameter `request`
        :param request: Request
        """
        self.request = request
        self.product = product

    async def html_processing(self) -> List[str]:
        """
        The method returns links to the  product in the List
        :return: List[str]
        """
        # product = str(input('Ведите название продукта (htmlHandler): ')) # Потом откоментируй
        links = []
        soup = BeautifulSoup(await self.request.request(self.product), 'lxml')
        for html in soup.select('div.offer-wrapper'):
            url = html.select_one('a.marginright5.link.linkWithHash.detailsLink')['href']
            links.append(url)
        return links

    async def get_links(self, html_product) -> None:
        links = []
        soup = BeautifulSoup(html_product, 'lxml')
        for html in soup.select(''):
            pass

