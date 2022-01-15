# BeautifulSoup 解析网页

## What is Beautiful Soup

BeautifulSoup是一个找信息好帮手，它能帮你又快又准地找到并提取网页中的信息，大大简化了使用难度。

Beautiful Soup is a library that makes it easy to scrape information from web pages.
It sits atop an HTML or XML parser, providing Pythonic idioms for iterating, searching,
and modifying the parse tree.


我们总结一下爬网页的流程, 让你对 BeautifulSoup 有一个更好的定位.
* 选择要爬的网址 (url)
* 使用 python 登录上这个网址 (urlopen等)
* 读取网页信息 (read() 出来)
* 将读取的信息放入 BeautifulSoup
* 使用 BeautifulSoup 选取 tag 信息等 (代替正则表达式)

## Install beautifulSoup

```
pip install beautifulsoup4
```

## 安装解析器
Beautiful Soup need parser to analyze html, so you need to install a parser.

```
pip install lxml
```

Refer to https://www.crummy.com/software/BeautifulSoup/bs4/doc.zh/#id13


