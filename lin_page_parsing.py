#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_urls = ganji['item_urls']
item_info = ganji['item_info']

url = 'http://zhuanzhuan.ganji.com/detail/748440948882915332z.shtml'
def get_item_url(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for url in soup.select(' td.t a'):
        url = url.get('href').split('?')[0]
        item_urls.insert_one({'url': url})
        print(url)


def get_item_info(url):
    wb_data = requests.get(url)
    wb_data.encoding = 'utf-8'
    soup = BeautifulSoup(wb_data.text, 'lxml')
    # if 'zhuanzhuan' in url:
    #     titles = soup.select('div.box_left_top h1')
    #     prices = soup.select('div.price_li > span > i')
    #     districts =soup.select('div.palce_li > span > i')
    #     for title, price, district in zip(titles, prices, districts):
    #         data = {
    #             'title': title.get_text(),
    #             'price': price.get_text(),
    #             'district': district.get_text(),
    #             'url': url
    #         }
    #         print(data)
    # else:
    #     print('old')
    # titles = soup.select('#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')
    prices = soup.select('f22.fc-orange.f-type')
    print(prices)
    # districts = soup.select('#wrapper > div.content.clearfix > div.leftBox > div > div > ul > li')
    # for title, price, district in zip(titles, prices, districts):
    #     data = {
    #         'title': title.get_text(),
    #         'price': price.get_text(),
    #         'district': district.get_text(),
    #         'url': url
    #     }
    #     print(data)
get_item_info(url)