import requests
import webbrowser

# send get request with url parameters
start_url = 'http://baidu.com/s'
param = {'wd': 'morvanpython'}
r = requests.get(start_url, params=param)
print(r.url)
webbrowser.open(r.url) #打开默认浏览器, 观看百度的搜索页面

# send post request with data
start_url = 'http://pythonscraping.com/pages/files/processing.php'
data = {'firstname': 'Eric', 'lastname': 'Yang'}

r = requests.post(start_url, data=data)
print(r.text)