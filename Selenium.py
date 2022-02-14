import os
import requests
import pandas as pd
from time import sleep
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains

chrome_options = webdriver.ChromeOptions()
chrome_options.add_argument("--disable-notifications")

driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=chrome_options)

# 1. Testing a website

## Loading the website
driver.get("https://pricebaba.com/") 
driver.maximize_window()

## Testing element hover capabilities
hover_over = driver.find_element_by_id("Mobiles-main")

hover = ActionChains(driver).move_to_element(hover_over)
hover.perform()

## Clicking floatable elements
driver.find_element_by_xpath('//*[@id="Mobiles"]/div[1]/a[1]').click()

## Back to homepage
driver.find_element_by_xpath('//*[@id="mainBody"]/div[1]/div[3]/div[1]/div[1]/div/ul/li[1]/a/img').click()

## Testing static elements
driver.find_element_by_xpath('//*[@id="Mobiles-main"]/a').click()
driver.find_element_by_xpath('//*[@id="mainBody"]/div[1]/div[6]/div[6]/div/div[1]/div[2]/ul/li[1]/a/div[1]/div/img').click()


# 3. Extracting Data from a social media platform - Facebook

email_id = <emailid>
password = <password>

driver.get("https://www.facebook.com/friends/list") 
driver.maximize_window()
  
driver.find_element_by_xpath('//*[@id="pageFooter"]/ul/li[11]/a').click()
driver.implicitly_wait(10)
driver.find_element_by_xpath('//*[@id="email"]').send_keys(email_id)
driver.find_element_by_xpath('//*[@id="pass"]').send_keys(password)
driver.find_element_by_xpath('//*[@id="loginbutton"]').click()

driver.implicitly_wait(15)
driver.find_element_by_xpath('//*[@id="mount_0_0_vE"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div/div[1]/div/div/div[1]/div/div/div[1]/div[1]/ul/li[1]/div/a/div[1]/div[2]/div/div/div/div/span/span').click()
driver.find_element_by_xpath('//*[@id="mount_0_0_vE"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div/div[4]/a/div[1]').click()

friends = int(driver.find_element_by_xpath('//*[@id="mount_0_0_vE"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]/div/div[2]/div[1]/div[2]/div/div[3]/div/div/div/div/div/h2/span/span').text.split("friends")[0].strip())

element = driver.find_element_by_xpath('//*[@id="mount_0_0_vE"]/div/div[1]/div/div[3]/div/div/div[1]/div[1]/div[1]')

friendsdata = element.get_attribute('outerHTML')

s = BeautifulSoup(friendsdata, 'html.parser') 

# Extract Friends Profile Link
friendsList = s.find_all('a')
friendsList = [pt['href'] for pt in friendsList]
friendsList = [pt for pt in friendsList if len(pt)>20]

# Extract Friends Name
friendsName = s.find_all('span',{'class':'d2edcug0 hpfvmrgz qv66sw1b c1et5uql lr9zc1uh jq4qci2q a3bd9o3v lrazzd5p oo9gr5id'})
friendsName = [pt.get_text() for pt in friendsName]

# Create Dataframe to Store Friends Details
friends_data = pd.DataFrame({"Name":friendsName,"Profile Link":friendsList})
