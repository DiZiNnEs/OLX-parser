from typing import Dict

from aiohttp import ClientSession


class Request:
    def __init__(self, user_agent: Dict, product_name: str) -> None:
        """
        Constructor takes one parameter `user_agent`
        :param user_agent: Dict
        """
        self.user_agent = user_agent
        self.product_name = product_name

    async def request(self) -> str:
        """
        First request to get pages
        :param product: str
        :return: str
        """
        session = ClientSession()
        async with session.get(headers=self.user_agent,
                               url=f'https://www.olx.kz/kokshetau/q-{self.product_name}') as response:
            content = await response.text()
        await session.close()

        return content

    async def request_for_links(self, link) -> str:
        """
        Second request to get another pages
        :param link:
        :param product: str
        :return: str
        """
        session = ClientSession()
        async with session.get(headers=self.user_agent,
                               url=link) as response:
            content = await response.text()
        await session.close()

        return content
