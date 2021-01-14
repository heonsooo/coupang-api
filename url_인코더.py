import urllib
from urllib import parse

# 한글 -> URL 인코딩 (아스키 코드)
lo = urllib.parse.quote('전기장판')
print(lo)

# URL (아스키 코드) ->  한글 인코딩
en = urllib.parse.unquote('https://www.coupang.com/np/search?component=&q=%EC%A0%84%EA%B8%B0%EC%9E%A5%ED%8C%90&channel=user')
print(en)


print( lo == '%EC%A0%84%EA%B8%B0%EC%9E%A5%ED%8C%90')
