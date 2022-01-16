from os import POSIX_FADV_DONTNEED
import requests
from bs4 import BeautifulSoup
import re

# This is URL for a baidutieba post
start_urls = [
    'https://tieba.baidu.com/p/7630316132',
    'https://tieba.baidu.com/p/7231728012']


def parse_post(post):
    soup = BeautifulSoup(post, 'lxml')
    content = soup.find_all('div', {'class': "d_post_content j_d_post_content"})
    imgs = content[0].find_all('img', {'class': 'BDE_Image'})
    for img in imgs:
        file_name = img['src'].split('/')[-1]
        r = requests.get(img['src'], stream=True)
        with open('easy_scrapy/3_requests/imges/'+file_name, 'wb') as f:
            for chunk in r.iter_content(chunk_size=32):
                f.write(chunk)


for url in start_urls:
    post = requests.get(url).text
    parse_post(post)
