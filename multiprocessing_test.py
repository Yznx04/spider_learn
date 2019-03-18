import multiprocessing as mp
from lxml import etree
import requests
import time

headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit"
                         "/537.36 (KHTML, like Gecko) "
                         "Chrome/72.0.3626.121 Safari/537.36"}
#豆瓣的电影TOP10
r_url = "https://movie.douban.com/chart"


def crawl(surl):
    """
    获取页面的信息
    :param surl:
    :return: 返回请求成功的对象，在这里不做过多处理，不然会出错
    """
    return requests.get(url=surl, headers=headers).content.decode()


def get_url_list(response):
    """
    获取每一个电影的URL
    :param response:
    :return: 返回一个URL列表
    """

    response = etree.HTML(response)
    return response.xpath('//*[@id="content"]/div/div[1]/'
                          'div/div/table/tr/td[2]/div/a/@href')


def get_content(resonse):
    """
    获取到我们想要的数据
    :param resonse:
    :return: 返回电影的名称和导演
    """
    resonse = etree.HTML(resonse)
    name = resonse.xpath('//*[@id="content"]/h1/span[1]//text()')
    author = resonse.xpath('//*[@id="info"]/span[1]/span[2]//text()')
    return name, author


if __name__ == '__main__':
    t1 = time.time()
    home = crawl(r_url)
    url_list = get_url_list(home)
    pool = mp.Pool()
    now_crawl = [pool.apply_async(crawl, (urls,)) for urls in url_list]
    contents = [j.get() for j in now_crawl]
    cont = [pool.apply_async(get_content, (c,)) for c in contents]
    for c in cont:
        print(c.get())
    print("use time:", time.time()-t1)
