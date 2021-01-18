#Code to automate playing songs on youtube using seleniium

# -*- coding: utf-8 -*-
'''By Ajay'''

#importing required libraries
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options

#Necessary setting to use selenium with brave browser
options=Options()
options.binary_location='C:\\Program Files (x86)\\BraveSoftware\\Brave-Browser\\Application\\brave.exe'

#Web automation to play songs
song_info=input('Enter song name: ')
print(song_info)
browser=webdriver.Chrome(options=options,executable_path='F:\\chromedriver.exe')                            
browser.get('https://music.youtube.com/')
link1=WebDriverWait(browser,5).until(ec.element_to_be_clickable((By.XPATH,"/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/paper-icon-button[1]")))
link1.click()
find=WebDriverWait(browser,5).until(ec.element_to_be_clickable((By.XPATH,"/html/body/ytmusic-app/ytmusic-app-layout/ytmusic-nav-bar/div[2]/ytmusic-search-box/div/div[1]/input")))
find.send_keys(song_info)
find.send_keys(Keys.ENTER)
song=WebDriverWait(browser,5).until(ec.element_to_be_clickable((By.XPATH,"/html/body/ytmusic-app/ytmusic-app-layout/div[3]/ytmusic-search-page/ytmusic-section-list-renderer/div[2]/ytmusic-shelf-renderer[1]/div[2]/ytmusic-responsive-list-item-renderer/div[1]/ytmusic-item-thumbnail-overlay-renderer/div")))
song.click()
