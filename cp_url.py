# 제품 이름 입력하면 100개 제품 나오는 카테고리 열어줌
import hmac
import hashlib
import os
import time
import requests
import json
import urllib
from urllib import parse

# 쿠팡파트너스 약자
import cp 

#####################
# 개인 정보 !!!
ACCESS_KEY = ''
SECRET_KEY = ''
#####################


### 원하는 제품  ###
product = cp.keyword                        # 네이버 top100에서 인기 검색어 상위 10 키워드 추출하여(cp.py) 순서대로 키워드 가져오기  
product = urllib.parse.quote(product)       # 해당 키워드를 url에 첨부하도록 아스키코드 변환
link = 'https://www.coupang.com/np/search?component=&q='+product+'&channel=user'         # 해당 키워드 가진 100개 제품이 있는 url을 link에 저장
###################


# 쿠팡 API) 해당 키워드의 링크 입력하고  쿠팡파트너스 링크로 변환해주기.
REQUEST_METHOD = "POST"                                                     
DOMAIN = "https://api-gateway.coupang.com"
URL = "/v2/providers/affiliate_open_api/apis/openapi/v1/deeplink"

# 원하는 쿠팡 링크를 REQUEST에 
REQUEST = { "coupangUrls": [link]  }


# HMAC Signature 생성 (쿠팡 개발자 docs 참고)
def generateHmac(method, url, secretKey, accessKey):
    path, *query = url.split("?")
    os.environ["TZ"] = "GMT+0"
    datetime = time.strftime('%y%m%d',time.gmtime()) + 'T' + time.strftime('%H%M%S',time.gmtime()) + 'Z' 
    message = datetime + method + path + (query[0] if query else "")

    signature = hmac.new(bytes(secretKey, "utf-8"),
                         message.encode("utf-8"),
                         hashlib.sha256).hexdigest()

    return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(accessKey, datetime, signature)


# 발급받은 HMAC이용하여 쿠팡 API 접근 및 이용 권한 획득
authorization = generateHmac(REQUEST_METHOD, URL, SECRET_KEY, ACCESS_KEY)

# 쿠팡 API 통해서 위에서 입력한 키워드(제품)의 쿠팡파트너스 링크 획득
url = "{}{}".format(DOMAIN, URL)
resposne = requests.request(method=REQUEST_METHOD, url=url,
                            headers={
                                "Authorization": authorization,
                                "Content-Type": "application/json"
                            },
                            data=json.dumps(REQUEST)
                            )
print(resposne.json())


# url이 총 3가지 반환되는데, 그 중 가장 짧은 링크를 고르기위한 함수 생성  
# url_list = [ x for x in resposne.json()['data']]

for i in range(len(url_list)):
    result = url_list[i]['shortenUrl'] 

# result : 해당 키워드의 쿠팡파트너스링크 -> main.py 에서 사용 예정
