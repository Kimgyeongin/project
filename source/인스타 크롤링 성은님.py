# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 15:19:08 2019

@author: OliviaKim
"""

import time
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from bs4 import BeautifulSoup
import numpy as np
import matplotlib.pyplot as plt
import platform
%matplotlib inline
from time import sleep
from matplotlib import font_manager, rc
plt.rcParams['axes.unicode_minus'] = False

if platform.system() == 'Darwin':
   rc('font', family='AppleGothic')
elif platform.system() == 'Windows'    :
   path = "c:/Windows/Fonts/malgun.ttf"
   font_name = font_manager.FontProperties(fname=path).get_name()
   rc('font', family=font_name)
else:
   print('Unknown system')

plt.rcParams['axes.unicode_minus'] = False
import re

driver= webdriver.Chrome('../data/chromedriver')

driver.get('https://www.instagram.com/explore/tags/%EB%B9%84%EB%B9%84%EA%B3%A0%EB%A7%8C%EB%91%90/')  #사이트주소 

time.sleep(5)
xpath_s1 = """//*[@id="react-root"]/section/main/article/div[1]/div/div/div[1]/div[1]"""
set1 = driver.find_element_by_xpath(xpath_s1).click()

time.sleep(2)

box1 = []
box2 = [] 
box3 = []


for n in range(1,5000):
    page1 = driver.page_source
    soup1 = BeautifulSoup(page1)
    a = soup1.find_all('div','C4VMK')
    a1 = soup1.find_all('div','C4VMK')[0]
    a1 = a1.find_all('span')[0].text
    b1 = re.split('#',a1)[0]
    b2 = re.split('#',a1)[1:]
    box1.append(b1)
    box2.append(b2)
    for i in range(1,len(a)):
        a2 = soup1.find_all('div','C4VMK')[i]
        a2 = a2.find_all('span')[0].text
        box3.append(a2)
    try:
        xpath_s1 = """/html/body/div[4]/div[1]/div/div/a[2]"""
        set1 = driver.find_element_by_xpath(xpath_s1).click()
        time.sleep(2)
    except:
        xpath_s1 = """/html/body/div[4]/div[1]/div/div/a"""
        set1 = driver.find_element_by_xpath(xpath_s1).click()
        time.sleep(2)
   

    print(n)