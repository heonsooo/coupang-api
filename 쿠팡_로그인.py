from selenium import webdriver
import time

### 개인정보
id = ''
pw = ''


# 크롬 열기
driver = webdriver.Chrome('./chromedriver.exe')

# 웹사이트 들어가기
url = 'https://partners.coupang.com/#affiliate/ws/link/0/%EB%85%B8%ED%8A%B8%EB%B6%81'
driver.get(url)

# 최대화
driver.maximize_window()

# 아이디, 비밀번호
driver.find_element_by_css_selector('#login-email-input').send_keys(id)
driver.find_element_by_css_selector('#login-password-input').send_keys(pw)

# 로그인 버튼 클릭 
driver.find_element_by_css_selector('body > div.member-wrapper.member-wrapper--flex > div > div > form > div.login__content.login__content--trigger > button').click()

time.sleep(5)
