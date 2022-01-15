from bs4 import BeautifulSoup
from urllib.request import urlopen

# open and read web page, decode it if it contains Chinese
html = urlopen('https://mofanpy.com/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)

# 'lxml' is parser name
soup = BeautifulSoup(html, features='lxml')

# access html element by tag
print(soup.h1)

# search by tag name
all_href = soup.find_all('a')

# 用Python字典的形式, 用key来读取Tag的属性。
# 用.text或.get_text()取得Tag的Text文字。
print( [f"{a.text}: {a['href']}" for a in all_href] )
