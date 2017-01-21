#-*- coding: utf-8 -*-

from bs4 import BeautifulSoup
import requests
import pymongo

client = pymongo.MongoClient('localhost', 27017)
ganji = client['ganji']
item_urls = ganji['item_urls']
item_info = ganji['item_info']

headers = {
    'User-Agent': 'User-Agent:Mozilla/5.0 (Windows NT 6.1; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.87 Safari/537.36',
    'Cookie':'statistics_clientid=me; ganji_uuid=9769651850000317357162; ganji_xuuid=246bfca8-3ccd-42b7-9d0e-f09730a2f0eb.1482411057001; als=0; citydomain=bj; GANJISESSID=918c8c8404adc27f93c82f4c2992cdbc; __utmt=1; 58uuid=d8d378bd-e73a-4287-8af6-e89cb8582b5c; new_session=0; init_refer=; new_uv=8; ganji_login_act=1485013909068; lg=1; __utma=32156897.1067797694.1482411056.1484963290.1485013901.7; __utmb=32156897.3.10.1485013901; __utmc=32156897; __utmz=32156897.1485013901.7.5.utmcsr=bj.ganji.com|utmccn=(referral)|utmcmd=referral|utmcct=/bangong/; _gl_tracker=%7B%22ca_source%22%3A%22-%22%2C%22ca_name%22%3A%22-%22%2C%22ca_kw%22%3A%22-%22%2C%22ca_id%22%3A%22-%22%2C%22ca_s%22%3A%22self%22%2C%22ca_n%22%3A%22-%22%2C%22ca_i%22%3A%22-%22%2C%22sid%22%3A75443799378%7D'
    }

url = 'http://bj.ganji.com/bangong/23819687254584x.htm'
def get_item_url(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    for url in soup.select(' td.t a'):
        url = url.get('href').split('?')[0]
        item_urls.insert_one({'url': url})
        print(url)


def get_item_info(url):
    wb_data = requests.get(url)
    soup = BeautifulSoup(wb_data.text, 'lxml')
    if 'zhuanzhuan' in url:
        titles = soup.select('div.box_left_top h1')
        prices = soup.select('div.price_li > span > i')
        districts =soup.select('div.palce_li > span > i')
        for title, price, district in zip(titles, prices, districts):
            data = {
                'title': title.get_text(),
                'price': price.get_text(),
                'district': district.get_text(),
                'url': url
            }
            # print(data)
    else:
        titles = soup.select('#wrapper > div.content.clearfix > div.leftBox > div.col-cont.title-box > h1')
        prices = soup.select('.f22.fc-orange.f-type')
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