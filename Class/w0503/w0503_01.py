# 역대관객순
# 이미지, 제목, 누적관객수, 날짜
# 이미지 저장까지 해야함
# 2023,2022,2021,2020

# 콘솔창에 출력하고, db에 저장하시오
# daum_movie 테이블
# dno 시퀀스
# title 문자타입(100)
# img 문자티입 (100)
# audience 누적관객수 숫자타입(10)
# ddate 날짜타입

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
conn = oracledb.connect(user="ora_user",password="1111",dsn="localhost:1521/xe")
cursor = conn.cursor()
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36","Accep-Language":"ko-KR,ko;q=0.9,en-US;q=0.8,en;q=0.7"}
browser = webdriver.Chrome()
browser.maximize_window()


url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser.get(url)
time.sleep(2)
# 2023 년 페이지 이동


i = 0
for r in range(2,5):
    elem = browser.find_element(By.XPATH,f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li{[r]}/a').click()
    time.sleep(2)
    soup = BeautifulSoup(browser.page_source,"lxml")
    all = soup.find("ul",{"class":"c-list-basic ty_flow35"})
    movie_list = all.find_all("li")
    for i in range(10) :
        # 이미지 따오기
        img = movie_list[i].find("img")['src']
        print("이미지 :  ",img)
        time.sleep(1)
        with open(f"movie_{i}.jpg","wb") as f:
            re_img = requests.get(img) #url링크를 다시 읽어와야 함.
            f.write(re_img.content) # 파일이름의 내용을 저장
        # 타이틀 따오기
        title = movie_list[i].find("strong",{"class":"tit-g clamp-g"}).text
        print("제목 : ",title)
        time.sleep(1)

        # 누적관객수 따오기
        audience = movie_list[i].find("p",{"class":"conts-desc clamp-g"}).text
        print ("누적 관객수 : ",audience)
        time.sleep(1)

        # 날짜 따오기
        ddate = movie_list[i].find("span",{"class":"conts-subdesc clamp-g"}).text[0:-2].replace('.','/')
        print("날짜 : ",ddate)
        
        i+=1
        
        sql = f"insert into daum_movie  values (seq_dno.nextval,'{img}','{title}'\
        ,'{audience}','{ddate}')"
        cursor.execute(sql)
    
    
    
    
    
    
    
    

print("-"*30)

cursor.execute('commit')
cursor.close()
conn.close()