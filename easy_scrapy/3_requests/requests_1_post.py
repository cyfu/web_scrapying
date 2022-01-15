import requests
import webbrowser

# send get request with url parameters
start_url = 'http://baidu.com/s'
param = {'wd': 'morvanpython'}
r = requests.get(start_url, params=param)
print(r.url)
webbrowser.open(r.url) #打开默认浏览器, 观看百度的搜索页面
