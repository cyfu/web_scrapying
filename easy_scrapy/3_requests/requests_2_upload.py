import requests

# send post request to upload a picture file
start_url = 'https://pythonscraping.com/pages/files/processing2.php'
file = {'uploadFile': open('easy_scrapy/3_requests/imges/scrapy_python.png', 'rb')}

r = requests.post(start_url, files=file)
print(r.url)
print(r.text)
