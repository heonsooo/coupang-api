import hmac 
import hashlib 
import os
import time 
import requests 
import json 
import datetime
import urllib.parse 
import naver_shop


# 특정 키워드의 제품 상위 n개 가져오는 API 예제(https://jikun.kr/620# 블로그 참고)
limit = '5'
class Coupang: 
    def __init__(self): 
        self.access_key = ''
        self.secret_key = '' 
        self.method = 'GET' 
        self.DOMAIN = 'https://api-gateway.coupang.com' 
        
    # HMAC Signature 생성 (쿠팡 개발자 docs 참고)
    def generateHmac(self, url):
        path, *query = url.split("?") 
        os.environ["TZ"] = "GMT+0" 
        # 오류나서 cp_url.py랑 같게 만들었습니다. 
        datetime = time.strftime('%y%m%d',time.gmtime()) + 'T' + time.strftime('%H%M%S',time.gmtime()) + 'Z' 
        message = datetime + self.method + path + (query[0] if query else "") 
        signature = hmac.new(bytes(self.secret_key, "utf-8"), message.encode("utf-8"), hashlib.sha256).hexdigest() 
        
        return "CEA algorithm=HmacSHA256, access-key={}, signed-date={}, signature={}".format(self.access_key, datetime, signature) 
    
    # 인증 권한 획득 후 n개의 제품 정보 받는 함수  URL 맨뒤에서 개수 제한하기
    def search_coupang(self, keyword): 
        URL = "/v2/providers/affiliate_open_api/apis/openapi/products/search?keyword=" + keyword + "&limit={}".format(limit) 
        url = "{}{}".format(self.DOMAIN, URL) 
        response = requests.request(method=self.method, url=url, headers={"Authorization": self.generateHmac(URL),"Content-Type": "application/json;charset=UTF-8"}) 
        resdata = json.dumps(response.json(), indent=4, ensure_ascii=False)
        resdata = json.loads(resdata)
        return resdata



# naver_shop.result : 네이버 쇼핑 상위 10개 제품 키워드 
# 시간에 따라 키워드 바꿔서 출력하도록 설정 (보통 8시에 컴퓨터를 키기에 8시부터 한시간에 하나씩 출력하게 한 후 hr-8(8시가 0으로 시작) 값이 10일때부터 키워드 입력받도록)
hr = datetime.datetime.now().hour
n = hr =8
if n < 10:
    best = naver_shop.result[n]
else:
    best = input()

# 이때 이 키워드가 main.py 와 cp_url.py에 사용됩니다.
keyword = best
keyword1 = urllib.parse.quote(keyword)

# n개의 제품 정보 result에 저장
result = Coupang().search_coupang(keyword1)

# 필요한 데이터(제품이름, 가격, 이미지, 링크, 순위)만 추출하고 result_list에 담기
result= result['data']
result = result['productData']
result_list = []
for i in result:
    j = list(i.values())
    result_list.append(j[1:5])

#필요한 정보 중 사진은 파일로 저장, 나머지는 products에 다시 저장한다.  이 products는 main.py(티스토리 api)에서 사용한다.
products = []
for j,n in zip(k,range(int(limit))):
    urllib.request.urlretrieve(j.pop(2), './pic/product{}.jpg'.format(n))
    products.append(j)


# 제품 정보 예시
'''
{'productId': 332473915, 
'productName': 'Apple 에어팟 프로, MWP22KH/A', 
'productPrice': 278800, 
'productImage': 'https://static.coupangcdn.com/image/retail/images/2019/11/07/18/8/4febc558-85b2-48a8-816e-0940180702df.jpg', 
'productUrl': 'https://link.coupang.com/re/AFFSDP?lptag=AF6221472&pageKey=332473915&itemId=1062243893&vendorItemId=70440310797&traceid=V0-153-c776b7d074aa1d0a',
'keyword': '에어팟프로', 
'rank': 1, 
'isRocket': False, 
'isFreeShipping': True},
'''