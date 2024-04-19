from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import loginInfo
from selenium.webdriver.common.keys import Keys
import random

browser = webdriver.Firefox()
browser.get("https://twitter.com/")

time.sleep(3)

browser.find_element(By.XPATH, "/html/body/div/div/div/div[2]/main/div/div/div[1]/div/div/div[3]/div[5]/a/div/span/span").click()

time.sleep(5)

username = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[5]/label/div/div[2]/div/input")

username.send_keys(loginInfo.username)

time.sleep(2)

browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div/div/div/div[6]/div").click()

time.sleep(5)

password = browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[1]/div/div/div[3]/div/label/div/div[2]/div[1]/input")

password.send_keys(loginInfo.password)

time.sleep(2)

browser.find_element(By.XPATH, "/html/body/div/div/div/div[1]/div[2]/div/div/div/div/div/div[2]/div[2]/div/div/div[2]/div[2]/div[2]/div/div[1]/div/div/div/div/span/span").click()

time.sleep(10)

searchArea = browser.find_element(By.XPATH, "/html/body/div[1]/div/div/div[2]/main/div/div/div/div[2]/div/div[2]/div/div/div/div[1]/div/div/div/form/div[1]/div/div/div/label/div[2]/div/input")

time.sleep(1)

searchArea.send_keys("#yazilimayolver")

time.sleep(2)

searchArea.send_keys(Keys.RETURN)

time.sleep(5)


lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    
    time.sleep(5)
    
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True
time.sleep(5)


i = 0

while i < 500:
    try:
        liker = browser.find_element(By.CSS_SELECTOR, "[data-testid=like]")
        liker.click()
        i += 1
    except:
        pass

































