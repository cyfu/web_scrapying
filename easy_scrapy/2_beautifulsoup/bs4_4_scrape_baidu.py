from urllib.request import urlopen
from bs4 import BeautifulSoup
import re
import random

start_url = 'https://baike.baidu.com/item/%E8%8A%B1%E5%B2%97%E5%B2%A9'

html = urlopen(start_url).read().decode('utf-8')
soup = BeautifulSoup(html, features='lxml')

# Get basic info div
basic_info_divs = soup.find_all('div', {'class': 'basic-info'})
print(basic_info_divs)

labels = basic_info_divs[0].find_all('dt', {'class': 'basicInfo-item name'})
values = basic_info_divs[0].find_all('dd', {'class': 'basicInfo-item value'})
if len(labels) == len(values):
    for ind in range(len(labels)):
        print(f"{labels[ind].get_text()}: {values[ind].get_text()}")


# scrape 解读词条背后的知识
tashuo_divs = soup.find_all('div', {'id': 'tashuo_bottom', 'class': 'tashuo-bottom'})
tashuo_items = tashuo_divs[0].find_all('li', {'class': 'tashuo-item J-item', 'data-tashuoid': re.compile('.+?')})

for tashuo_item in tashuo_items:
    titles = tashuo_item.find_all('p', {'class': 'title'})
    title = titles[0].get_text()
    print(title)
    urls = tashuo_item.find_all('a', {'class': 'cover'})
    url = urls[0]['href']
    print(url)
