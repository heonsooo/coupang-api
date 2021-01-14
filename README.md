# Coupang_API
쿠팡_API 활용


- 쿠팡파트너스 API를 활용합니다.

#### cp_url.py
- 쿠팡파트너스 API를 이용해 원하는 키워드의 100개 항목이 있는 URL을 얻습니다.

#### cp.py
- 쿠팡파트너스 API를 이용해 원하는 키워드의 상위 제품 N개를 저장합니다.

***

#### 왜 쿠팡파트너스 API를 사용하였는가? 

1. 이전에 조코딩-주식 자동 트레이딩 파이썬을 구현 후 잠깐의 시간을 투자해 앞으로도 계속 **자동**으로  
  수입이 생길 수 있는 자동화 파이프라인을 만들면 좋겠다고 생각했습니다. 
    
2. 그렇게 네이버 쇼핑에서 인기 제품들을 쿠팡파트너스에서 검색 후 블로그에 포스팅하는 시스템을 생각했습니다.   
   
3. 쿠팡 파트너스 홈페이지에서 셀레니움을 통해 제품을 파싱해오려고 했지만,      
크롬드라이버로 쿠팡파트너스에는 **무한로딩**이되며 로그인이 되지 않았습니다. --- 문제점 1)   
   
4. 방법을 찾던 중 쿠팡파트너스 API가 있는것을 확인 후 아이디, 비밀번호 키를 발급받았습니다. --- 해결 1)    



