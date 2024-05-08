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


url = "https://flight.naver.com/flights/domestic/GMP-CJU-20240626/CJU-GMP-20240627?adult=1&fareType=YC"
browser.get(url)
time.sleep(10)
soup = BeautifulSoup(browser.page_source,"lxml")
all = soup.find("div",{"class":"domestic_flight_content__ZPRcn"})
air_list = all.find_all("div",{"class":"domestic_Flight__sK0eA"})


#//*[@id="__next"]/div/main/div[6]/div/div[2]/div[2]/div/div[1]/div/div[2]/span[1]/b
#//*[@id="__next"]/div/main/div[6]/div/div[2]/div[3]/div/div[1]/div/div[2]/span[1]/b
 
# 항공사 따오기
airline = browser.find_element(By.XPATH,'//b[@class="airline_name__Tm2wJ"]').text
print("항공사 : ",airline)

# 출발시간 따오기
departure_time = browser.find_element(By.XPATH,'//b[@class="route_time__-2Z1T"]').text
print("출발시간 : ",departure_time)

# 도착시간 따오기
arrival_time = browser.find_element(By.XPATH,'//b[@class="route_time__-2Z1T"]').nextSibling.text
print("출발시간 : ",arrival_time)

# 소요시간 따오기
flight_time = browser.find_element(By.XPATH,'//i[@class="route_info__1RhUH"]').text
print("출발시간 : ",flight_time)

# 가격 따오기
price = browser.find_element(By.XPATH,'//i[@class="domestic_num__2roTW"]').text
print("가격 : ",price)

 
