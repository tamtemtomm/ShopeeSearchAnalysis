import requests
import json
import pandas as pd
from seleniumwire import webdriver
from seleniumwire.utils import decode

# cari = 'laptop'
# header = {
#     'user-agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/109.0.0.0 Safari/537.36'}
# url = 'https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword=laptop&limit=60&newest=0&order=desc&page_type=search&scenario=PAGE_GLOBAL_SEARCH&version=2&view_session_id=3f833266-9c9a-4dfb-a946-95c709465ffb'
# req = requests.get(url, headers=header).json()

# print(req)

driver = webdriver.Chrome()
url = 'https://shopee.co.id/search?keyword=laptop'
driver.get(url)

for request in driver.requests:
    if request.response:
        if request.url.startswith('https://shopee.co.id/api/v4/search/search_items?by=relevancy&keyword='):
            # # STEP 1
            # body = request.response.body
            # print(body)
            
            # STEP 2 
            response = request.response
            body = decode(response.body, response.headers.get('Content-Encoding', 'Identity'))
            decoded_body = body.decode('utf8')
            json_data = json.loads(decoded_body)
            
            with open('shopee_raw.json', 'w') as f:
                json.dump(json_data, f, indent=2 )

