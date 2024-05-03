# 1.야놀자
# 2.검색창에 호텔입력
# 3.날짜선택 6월 5일 6월 6일
# 4. 검색ㅈ;ㄴ헹
# 5. 스크롤 이동 반복
# 6. 정보창이 띄워지면, 이미지, 제목, 평점, 평가수, 금액 저장하시오
# yanolja 테이블
# yno,img,title,grade,grade_num,price

import oracledb
import requests
import time
import random
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
# 화면이 나타나는 것을 확인
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pyautogui

headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()
url = "https://www.yanolja.com/?utm_source=google_sa&utm_medium=cpc&utm_campaign=20738115572&utm_content=160897187931&utm_term=kwd-327025203539&gad_source=1&gclid=CjwKCAjw88yxBhBWEiwA7cm6pT5FGOcAUcPyDLwId3DhHnltSZnfin7raDlh63_Oci_b2iO1alyTUxoCF8AQAvD_BwE"

browser.get(url)

# 파일저장

# with open("yanolja.html","w",encoding="utf-8") as f:
#     f.write(soup.prettify())
# 파일불러오기
# with open("yanolja.html","r",encoding="utf-8") as f:
#     soup = BeautifulSoup(f,"lxml")
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/section/header/section/a[2]/div/div').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[2]/div[1]/button').click()
time.sleep(2)
elem = browser.find_element(By.XPATH,"/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[4]").click()
time.sleep(2)
elem = browser.find_element(By.XPATH,"/html/body/div[4]/div/div/section/section[3]/div/div/div/div[2]/div/div[2]/div[2]/div/table/tbody/tr[2]/td[5]").click()
time.sleep(2)
elem = browser.find_element(By.XPATH,"/html/body/div[4]/div/div/section/section[4]/button").click()
time.sleep(2)
elem = browser.find_element(By.XPATH,'//*[@id="__next"]/div[1]/main/div/div[1]/form/div/div[1]/div/input')
elem.send_keys('호텔')
elem.send_keys(Keys.ENTER)
time.sleep(2)

soup = BeautifulSoup(browser.page_source,"lxml")
i = 1

all = soup.find("section",{"class":"PlaceListBody_placeListBodyContainer__1u70R"})
all2 = soup.find("div",{"class":"PlaceListBody_itemGroup__1V8Q3 PlaceListBody_textUnitList__HEDb3"})
print(all2)
# print (all)
# while True:
#     pyautogui.moveTo(500,500)
#     pyautogui.scroll(-500)
#     pyautogui.sleep(3)
    
 
# img = all2.find("div",{"class","PlaceListImage_imageText__2XEMn"})["style"]
# print("이미지 : ",img)
# title = all2.find("strong",{"class":"PlaceListTitle_text__2511B"}).text
# print("제목 : ",title)
# grade = all2.find("span",{"class":"Icon_icon__2BP_o PlaceListScore_star__2IZFX"}).nextSibling.text
# print("평점 : ",grade)
# grade_num = all2.find("span",{"class":"PlaceListScore_reviewInfo__3QSCU"}).text.strip()[1:-1]
# print("평가수 : ",grade_num)
# price = all2.find("span",{"class":"PlacePriceInfoV2_discountPrice__1PuwK"}).text
# print("금액 : ",price)



