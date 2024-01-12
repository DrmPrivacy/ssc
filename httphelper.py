import urllib3
import config
import json
import time
import random
def request(url, requestBody):
    try:
        # time.sleep(1)
        headers ={
        'Content-Type':'application/json;charset=UTF-8',
        'Cookie':config.Cookie,
        'Sec-Ch-Ua':'Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120',
        'Sec-Ch-Ua-Mobile':'?0',
        'Sec-Ch-Ua-Platform':'Windows',
        'Sec-Fetch-Dest':'empty',
        'Sec-Fetch-Mode':'cors',
        'Sec-Fetch-Site':'same-site',
        'User-Agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36',
        'Useragent':'5',
        'Origin':'https://www.sscha.com',
        'Referer':'https://www.sscha.com/'
        }
        proxy_url = random.choice(config.ProxyList)
        print(proxy_url)
        proxy = urllib3.ProxyManager(proxy_url,num_pools=1000, headers=headers, proxy_headers=headers)
        response = proxy.request(method='POST', url=url, body=json.dumps(requestBody), headers=headers)
        return response.json()
    except Exception as OF:
        print(OF)
        return None