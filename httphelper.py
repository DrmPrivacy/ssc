import urllib3
import config
import json
def request(url, requestBody):
    headers ={
    'Content-Type':'application/json;charset=UTF-8',
    'Cookie':config.Cookie,
    'Sec-Ch-Ua':'Not_A Brand";v="8", "Chromium";v="120", "Google Chrome";v="120',
    'Sec-Ch-Ua-Mobile':'?0',
    'Sec-Ch-Ua-Platform':'Windows',
    'Sec-Fetch-Dest':'empty',
    # 'Sec-Fetch-Mode':'cors',
    # 'Sec-Fetch-Site':'same-site',
    'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    # 'Useragent':'5',
    # 'Origin':'https://www.sscha.com',
    # 'Referer':'https://www.sscha.com/'
    }
    # response = requests.post(url=url, data=requestBody, headers=headers, verify=False)
    response = urllib3.request(method='POST', url=url, body=json.dumps(requestBody), headers=headers)
    print(response)
    return response.json()