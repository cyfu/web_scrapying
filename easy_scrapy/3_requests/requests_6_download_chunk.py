import requests

# send GET request to download image file
IMG_URL = 'https://static.mofanpy.com/img/description/learning_step_flowchart.png'
r = requests.get(IMG_URL, stream=True)  # stream=True allow stream loading

# save response to file chunk by chunk
with open('easy_scrapy/3_requests/imges/learning_step_flowchart2.png', 'wb') as f:
    for chunk in r.iter_content(chunk_size=32):
        f.write(chunk)
