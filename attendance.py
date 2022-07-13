
from re import sub
from typing import List

import pydantic

from selenium.webdriver import Chrome
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from time import sleep

#code is written for KBTU system wsp.kbtu.kz

class Login(pydantic.BaseModel):
    login: str
    password: str

account=Login(login='',password='')

options = webdriver.ChromeOptions()
options.add_experimental_option('excludeSwitches', ['enable-logging'])
options.add_argument("start-maximized")        
driver=Chrome(service=Service(ChromeDriverManager().install()),options=options) 

# url='https://wsp.kbtu.kz/'
# driver.get(url)
# sleep(5)
# #first page
# driver.find_element(By.XPATH,'//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div[1]/div').click()

# sleep(5)
# #login process
# inputTabs=driver.find_elements(By.TAG_NAME,'input')
# inputTabs[0].send_keys(account.login)
# inputTabs[1].send_keys(account.password)
# driver.find_element(By.XPATH,'//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[4]/td[3]/div').click()

# sleep(5)
# #going from news to mainmenu
# driver.find_element(By.XPATH,'//*[@id="News-2424563"]/div/div[2]/div/div[1]/div/div/div[1]').click()

# sleep(5)
# #searching attendance check link
# #driver.find_element(By.LINK_TEXT,'Отметка посещения занятия').click() #okey maybe different for dif languages LATER
# driver.find_element(By.XPATH,'//*[@id="ROOT-2521314"]/div/div[2]/div/div[2]/div/div[17]/div/div[2]/div/div[1]/div/div/div/div[25]/div/a').click()

# #this will go to https://wsp.kbtu.kz/RegistrationOnline 
# sleep(5)
# print(driver.find_elements(By.XPATH,"//div[@role = 'button']"))

# sleep(5)
#that was long way in extra case

url='https://wsp.kbtu.kz/RegistrationOnline'
driver.get(url)

sleep(1)
#login process
inputTabs=driver.find_elements(By.TAG_NAME,'input')
inputTabs[0].send_keys(account.login)
#sleep(1) #one time login was not inserted but password was, no clue why
inputTabs[1].send_keys(account.password)
driver.find_element(By.XPATH,'//*[@id="RegistrationOnline-1674962804"]/div/div[2]/div/div[2]/div/div/div/div/div/div/div/div/div[2]/div/table/tbody/tr[4]/td[3]/div').click()
sleep(1)
#this will go to https://wsp.kbtu.kz/RegistrationOnline 
buttons=driver.find_elements(By.XPATH,"//div[@role = 'button']")
if(len(buttons)>4):
    #if the archetype will be not button like then i'll change from clicking to just informing me by message from telegrambot
    i=len(buttons)
    while(i>4):
        buttons[i-1].click()  #this way even if my buttons are not changing immediately, it will click in order that does not distract the order of buttons in list
        i-=1
#sleep(3)
driver.close()

