import aiohttp
import requests
import time
import asyncio
from lxml import etree

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}

def crawl():
    return requests.get("https://movie.douban.com/chart", headers=headers).\
        content.decode()


def get_url(response):
    response = etree.HTML(response)
    return response.xpath('//*[@id="content"]/div/div[1]/'
                          'div/div/table/tr/td[2]/div/a/@href')


async def get_crawl(url):
    session = aiohttp.ClientSession()
    res = await session.get(url=url, headers=headers)
    result = await res.text()

    return result


if __name__ == '__main__':
    start = time.time()
    res = crawl()
    url_list = get_url(res)
    loop = asyncio.get_event_loop()
    tasks = [asyncio.ensure_future(get_crawl(url)) for url in url_list]
    loop.run_until_complete(asyncio.wait(tasks))
    for t in tasks:
        b = t.result()
        re = etree.HTML(b)
        name = re.xpath('//*[@id="content"]/h1/span[1]//text()')
        author = re.xpath('//*[@id="info"]/span[1]/span[2]//text()')
        print(name, author)
    end = time.time()
    print("use time:", end-start)
    
    """
    ['���ߣ�Ե��'] ['�Ƽҿ�', ' / ', '����']
['С͵���� ����������'] ['��֦ԣ��']
['����������'] ['����']
['���� Aquaman'] ['������']
['��������'] ['���']
['֩������ƽ������ Spider-Man: Into the Spider-Verse'] ['���������������', ' / ', '�˵á���ķ��', ' / ', '�޵��ᡤ��˹
��']
['�������ǿ����� Bohemian Rhapsody'] ['������������']
['����ְҵ ????'] ['�����']
['һ�Ƕ���'] ['����ɺ']
['�޵��ƻ���2�����ֻ����� Ralph Breaks the Internet'] ['�ƶ���Լ��˹��', ' / ', '���桤Ħ��']
use time: 1.9417905807495117

    """