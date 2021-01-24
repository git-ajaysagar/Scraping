#The following program downlaods the list of followers of any instagram user (except unfollowed private accounts).
#It can be modified to download list of 'followings' also. It has imported user credentials from a separate file called 'userpass.py'. One can mention 
#those things directly in this program itself.

# -*- coding: utf-8 -*-
'''By Ajay'''

#Importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from userpass import username,password,username_to_search  #userpass is the python file which contains the imported information
from bs4 import BeautifulSoup as bsp
import time

#Setting options to use brave browser
options=Options()
options.binary_location='Location of the brave browser application'

#Initializing chrome driver
driver='Location of the chrome driver'

#Making a browser object to use browser
browser=webdriver.Chrome(options=options,executable_path=driver)                            

#Getting login page of instagram
browser.get('https://www.instagram.com/accounts/login/?hl=en')

#Waiting for username input box and entering username 
user=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[1]/div/label/input')))
user.send_keys(username)

#Entering password
passw=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[2]/div/label/input')))
passw.send_keys(password)

#Logging in 
login=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'//*[@id="loginForm"]/div/div[3]')))
login.click()  

#Getting profile of the user whose followers going to get downloaded 
search=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/nav/div[2]/div/div/div[2]/input')))
search.send_keys(username_to_search)
time.sleep(1)
search.send_keys(Keys.ENTER)
time.sleep(1)
search.send_keys(Keys.ENTER)

#Clicking on followers list
followers=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')))
followers.click()
clik_followers=WebDriverWait(browser,10).until(ec.element_to_be_clickable((By.XPATH,'/html/body/div[4]/div/div/div[2]')))
clik_followers.click()

#Getting number of followers
follower_num=browser.find_element_by_xpath('/html/body/div[1]/section/main/div/header/section/ul/li[2]/a')
follower_num=follower_num.text.split(' ')
follower_num=int(follower_num[0])
print('Followers shown on page: ',follower_num)

#Scrolling through the followers list
scroll_list=[]
while True:  
    browser.execute_script('arguments[0].scrollTop = arguments[0].scrollTop + arguments[0].offsetHeight;', clik_followers)
    time.sleep(1)
    html_txt=clik_followers.get_attribute('outerHTML')
    scroll_num=html_txt.count('wFPL8')
    scroll_list.append(scroll_num)
    try:
        if scroll_list[-1]==scroll_list[-4]:   #Condition to stop scrolling when all the followers are loaded
            print(scroll_num,follower_num)
            break
    except:
        continue  
  
#Printing actual number of followers        
print('You actually have '+str(scroll_num)+' followers')  

#Parsing html which contains followers 
html_txt2=bsp(html_txt,'html.parser')
followers=html_txt2.find_all('div',class_='wFPL8')

#Removing unnecessary text from html and retrieving followers' names
followers_list=[]                          #List to store followers
for i in range(scroll_num):
    a_follower=followers[i]
    a_follower=str(a_follower)
    a_follower=a_follower.replace('<div class="wFPL8">','')
    a_follower=a_follower.replace('</div>','')
    followers_list.append(a_follower)      #Appending followers in the list
print(followers_list)                      #Printing followers list


