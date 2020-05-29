'''
    이클립스 또는 jupyter lab으로 실행해 보기  : 화면 캡처
'''
from selenium import webdriver
try:
    url = "http://www.daum.net"
    browser = webdriver.Chrome('C:/Work/chromedriver')
    browser.implicitly_wait(3)
    
    browser.get(url);
    browser.save_screenshot("daum_img.png")
    browser.quit()
    
    print('성공')
except Exception:
    print('에러')