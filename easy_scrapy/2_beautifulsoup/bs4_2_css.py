from bs4 import BeautifulSoup
from urllib.request import urlopen

# open and read web page, decode it if it contains Chinese
html = urlopen('https://mofanpy.com/static/scraping/list.html').read().decode('utf-8')
print(html)

# 'lxml' is parser name
soup = BeautifulSoup(html, features='lxml')

# search by tag name and css class name
month_list = soup.find_all('li', {'class': 'month'})
print( [li.text for li in month_list] )

# extract ul element first, then search ul element for li elements
jan = soup.find_all('ul', {'class': 'jan'})
print(type(jan))
for j in jan:
    jan_days = j.find_all('li')
    print(type(j))
    print([ li.get_text() for li in jan_days])
