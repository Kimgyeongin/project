# -*- coding: utf-8 -*-
"""
Created on Tue Jun 18 10:32:17 2019

@author: OliviaKim
"""

from time import sleep
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys 
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import csv


#starting a new browser session
browser = webdriver.Chrome('../data/chromedriver')
browser.maximize_window() #For maximizing window
browser.implicitly_wait(20) #gives an implicit wait for 20 seconds
#navigating to a webpage
browser.get('https://www.instagram.com/')

# make sure the browser stays open for 5sec
sleep(5)

#clean exit

login=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/article/div[2]/div[2]/p/a')
login.click()

sleep(2)
#로그인 데이터 입력하기
browser.find_elements_by_name("username")[0].send_keys("01040924744")
browser.find_elements_by_name("password")[0].send_keys("lamin4092.")

browser.find_element_by_xpath("//form[1]/div[3]/button[1]").submit()

sleep(2)
#로그인 버튼 누르기
login_button=browser.find_element_by_xpath('//*[@id="react-root"]/section/main/div/article/div/div[1]/div/form/div[4]/button/div')
login_button.click()

#검색창 누르기
search=browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input')
search.click()
ActionChains(browser).move_to_element(search).click().send_keys('양념치킨').perform()


name = browser.find_element_by_xpath('//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

ActionChains(browser).move_to_element(name).click().perform()

sleep(5)
post = browser.find_element_by_class_name('_9AhH0')
post.click()


load= browser.find_element_by_xpath('/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div[2]')

while True:
	try:
		button = WebDriverWait(load, 5).until(EC.visibility_of_element_located((By.XPATH, 
        	"/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li[1]")))
	except TimeoutException:
		break  # no more wines
	button.click()  # load more comments

csv_file = open('insta2.csv', 'wb')
writer = csv.writer(csv_file)
writer.writerow(['hashtag'])


hash_dict = {}



tag = browser.find_element_by_xpath("/html/body/div[3]/div[2]/div/article/div[2]/div[1]/ul/li[1]/div/div/div[2]/span").text
hash_dict["hashtag"] = tag
writer.writerow(hash_dict.values()) 


browser.back()


	


sleep(5)

search = browser.find_element_by_css_selector(
	'#react-root > section > nav > div._s4gw0._1arg4 > div > div > div._5ayw3._ohiyl > input')

ActionChains(browser)\
.move_to_element(search).click()\
.send_keys('laurasykora')\
.perform()

name = browser.find_element_by_xpath(
	'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

ActionChains(browser)\
.move_to_element(name)\
.click().perform()



sleep(5)
post = browser.find_element_by_class_name('_si7dy')
post.click()




load= browser.find_element_by_xpath(
	'/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]/a')

while True:
	try:
		button = WebDriverWait(load, 5).until(EC.visibility_of_element_located((By.XPATH, 
        	"/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]/a")))
	except TimeoutException:
		break  # no more wines
	button.click()  # load more comments






tag = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]").text
hash_dict["hashtag"] = tag
writer.writerow(hash_dict.values())



browser.back()


#############################



sleep(5)

search = browser.find_element_by_css_selector(
	'#react-root > section > nav > div._s4gw0._1arg4 > div > div > div._5ayw3._ohiyl > input')

ActionChains(browser)\
.move_to_element(search).click()\
.send_keys('laurasykora')\
.perform()

name = browser.find_element_by_xpath(
	'//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/div[2]/div[2]/div/a[1]/div')

ActionChains(browser)\
.move_to_element(name)\
.click().perform()



sleep(5)
post = browser.find_element_by_class_name('_si7dy')
post.click()




load= browser.find_element_by_xpath(
	'/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]/a')

while True:
	try:
		button = WebDriverWait(load, 5).until(EC.visibility_of_element_located((By.XPATH, 
        	"/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]/a")))
	except TimeoutException:
		break  # no more wines
	button.click()  # load more comments



tag = browser.find_element_by_xpath("/html/body/div[4]/div/div/div[2]/div/article/div[2]/div[1]/ul/li[2]").text
hash_dict["hashtag"] = tag
writer.writerow(hash_dict.values())



browser.back()


	
csv_file.close()