from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import loginInfo
from selenium.webdriver.common.keys import Keys

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

tweets = []

tweetfield = browser.find_elements(By.CSS_SELECTOR, '.css-1rynq56.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim')

for tweet in tweetfield:
    if tweet not in tweets:
        tweets.append(tweet.text)

lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
match=False
while(match==False):
    lastCount = lenOfPage
    
    time.sleep(5)
    
    tweetfield = browser.find_elements(By.CSS_SELECTOR, '.css-1rynq56.r-8akbws.r-krxsd3.r-dnmrzs.r-1udh08x.r-bcqeeo.r-qvutc0.r-37j5jr.r-a023e6.r-rjixqe.r-16dba41.r-bnwqim')

    
    for tweet in tweetfield:
        if tweet not in tweets:
            tweets.append(tweet.text)
    
    lenOfPage = browser.execute_script("window.scrollTo(0, document.body.scrollHeight);var lenOfPage=document.body.scrollHeight;return lenOfPage;")
    if lastCount == lenOfPage:
        match=True

time.sleep(5)

tweetcount = 1

with open("tweets.txt","w",encoding = "UTF-8") as file:
    for tweet in tweets:
        file.write(str(tweetcount) + ".\n" + tweet + "\n")
        file.write("***********************************\n")
        tweetcount += 1
time.sleep(10)

#browser.quit()




















