import requests

# send GET request to download image file
IMG_URL = 'https://static.mofanpy.com/img/description/learning_step_flowchart.png'
r = requests.get(IMG_URL)

# save response to file as a whole
with open('easy_scrapy/3_requests/imges/learning_step_flowchart.png', 'wb') as f:
    f.write(r.content)
