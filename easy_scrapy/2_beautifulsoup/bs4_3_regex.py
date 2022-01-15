from bs4 import BeautifulSoup
from urllib.request import urlopen
import re

# open and read web page, decode it if it contains Chinese
html = urlopen('https://mofanpy.com/static/scraping/table.html').read().decode('utf-8')
print(html)

# 'lxml' is parser name
soup = BeautifulSoup(html, features='lxml')

# search by tag name and attribe name (src), use regex match src value
img_list = soup.find_all('img', {'src': re.compile('.*?\.jpg')})
print( [img['src'] for img in img_list] )

# another example
course_links = soup.find_all('a', {'href': re.compile('\/tutorials.*')})
for link in course_links:
    print(link['href'])

# another example
tables = soup.find_all('table', {'id': 'course-list'})
for table in tables:
    courses = table.find_all('tr', {'class': 'ml'})
    print([course['id'] for course in courses])