from urllib.request import urlopen
import re

# open and read web page, decode it if it contains Chinese
html = urlopen('https://mofanpy.com/static/scraping/basic-structure.html').read().decode('utf-8')
print(html)

# use regEx to extract the title
title = re.findall(r"<title>(.+?)</title>", html)
print("Page title is:\n", title[0])

# use regEX to extract the paragraph
# Paragrahp has multiple lines, flags=re.DOTALL 对tab, new line不敏感
paragraph = re.findall(r"<p>(.+?)</p>", html, flags=re.DOTALL)
print("Page context is:\n", paragraph[0])

# find all href links in the page so that they can be used for further scrapying
urls = re.findall(r'href="(.+?)">', html)
print(urls)