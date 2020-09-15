from typing import Dict

from aiohttp import ClientSession
from asyncio import get_event_loop

from bs4 import BeautifulSoup


async def request_for_check_page(headers: Dict, url: str) -> None:
    session = ClientSession()
    async with session.get(headers=headers, url=url) as response:
        content = await response.text()
    await session.close()
    soup = BeautifulSoup(content, 'html.parser')
    url = soup.select('a.block.br3.brc8.large.tdnone.lheight24')

    for x in soup.select('a.block.br3.brc8.large.tdnone.lheight24'):
        print(x.select('href'))


user_agent = {
    'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.102 Safari/537.36'
}
olx_link = 'https://www.olx.kz/kokshetau/q-%D0%BA%D1%80%D0%BE%D0%BB%D0%B8%D0%BA/'


async def request(headers: Dict, url: str) -> str:
    session = ClientSession()
    async with session.get(headers=headers, url=url) as response:
        content = await response.text()
    await session.close()

    return content


async def html_processing() -> None:
    soup = BeautifulSoup(await request(user_agent, olx_link), 'html.parser')
    for html in soup.select('div.offer-wrapper'):
        title = html.select('a.marginright5.link.linkWithHash.detailsLink>strong')
        price = html.select('p.price>strong')
        data = html.select('small.breadcrumb.x-normal>span')

        print(f'''
Название товара: {title},
Цена товара: {price},
Дата публикации: {data}
        ''')


if __name__ == '__main__':
    loop = get_event_loop()
    # loop.run_until_complete(html_processing())
    loop.run_until_complete(
        request_for_check_page(user_agent, 'https://www.olx.kz/kokshetau/q-%D0%BA%D1%80%D0%BE%D0%BB%D0%B8%D0%BA/'))
