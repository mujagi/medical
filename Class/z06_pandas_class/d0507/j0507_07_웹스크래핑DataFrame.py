
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


url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
browser.get(url)
time.sleep(2)
movie_list = {}
year_list = []
title_list = []
viewer_list = []
rating_list = []
r = 6
for i in range(5):
    url = "https://search.daum.net/search?w=tot&q=%EC%97%AD%EB%8C%80%EA%B4%80%EA%B0%9D%EC%88%9C%EC%9C%84&DA=MOR&rtmaxcoll=MOR"
    browser.get(url)
    time.sleep(2)
    elem = browser.find_element(By.XPATH,f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[{r}]/a').click()
    time.sleep(2)
    year = browser.find_element(By.XPATH,f'//*[@id="morColl"]/div/c-container/div[2]/c-carousel/div/ul/li[{r}]/a').text
    print("년도 : ",year)
    year_list.append(year)
    time.sleep(1)
    
    title = browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[2]/div[1]/c-title/strong').text
    print("제목 : ",title)
    title_list.append(title)
    time.sleep(1)
    
    viewer = browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[2]/div[2]/c-contents-desc/p/a').text[3:-2].replace(",","")
    print("누적 관객수 : ",int(viewer))
    viewer_list.append(viewer)
    
    elem = browser.find_element(By.XPATH,'//*[@id="mor_history_id_0"]/div/div[1]/div/div[1]/c-flicking-item/c-layout/div/c-list-doc/ul/li[1]/c-doc/div/div[2]/div[1]/c-title/strong/a').click()
    time.sleep(1)
    
    
    rating = browser.find_element(By.XPATH,'//*[@id="em1Coll"]/div/c-container/c-card[1]/div/c-doc-content/div/div[2]/c-list-grid-desc/dl/dd[5]/c-link/a/c-star/span').text[2:-4]
    print("평점 : ",rating)
    rating_list.append(rating)
    time.sleep(1)
    r-=1
movie_list['year'] = year_list
movie_list['title'] = title_list
movie_list['veiwer'] = viewer_list
movie_list['rating'] = rating_list


import pandas as pd
dt = pd.DataFrame(movie_list)
print(dt)