import os
import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

email_id = <emailid>
password = <password>

# FACEBOOK

driver.get("https://www.facebook.com/friends/list") 
driver.maximize_window()
  
driver.find_element_by_xpath('//*[@id="pageFooter"]/ul/li[11]/a').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email_id)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()
