from selenium import webdriver
from selenium.webdriver.common.by import By
import random
import time

browser = webdriver.Firefox()

url = "https://www.uludagsozluk.com/k/atat%C3%BCrk/"

pagecount = 1
entries = []
entrycount = 1

while pagecount <= 3:
    randompage = random.randint(1,16)
    newurl = url + str(randompage)
    browser.get(newurl)

    elements = browser.find_elements(By.CSS_SELECTOR, '.entry-body')
    for element in elements:
        entries.append(element.text)
    time.sleep(3)
    pagecount += 1

with open("entries.txt","w",encoding = "UTF-8") as file:
    for entry in entries:
        file.write(str(entrycount) + ".\n" + entry + "\n")
        file.write("***********************************\n")
        entrycount += 1

browser.close()
