from selenium.webdriver.common.by import By
from selenium import webdriver
import time
import logininfo
from selenium.webdriver.common.keys import Keys

browser = webdriver.Firefox()
browser.get("https://www.instagram.com/")

time.sleep(3)

login_username = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[1]/div/label/input")

login_password = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[2]/div/label/input")

login_username.send_keys(logininfo.username)

login_password.send_keys(logininfo.password)

time.sleep(3)

login_button = browser.find_element(By.XPATH, "//*[@id='loginForm']/div/div[3]").click()

time.sleep(15)

simdi_degil_button = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]")

simdi_degil_button.click()

time.sleep(8)

profil_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[2]/div/div/span/span").click()

time.sleep(5)

takipci_button = browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[2]/div[2]/section/main/div/header/section/ul/li[2]/a").click()

time.sleep(5)

jscommand = """
followers = document.querySelector(".x7r02ix.xf1ldfh.x131esax.xdajt7p.xxfnqb6.xb88tzc.xw2csxc.x1odjw0f.x5fp0pe");
followers.scrollTo(0, followers.scrollHeight);
var lenOfPage=followers.scrollHeight;
return lenOfPage;



"""


lenOfPage = browser.execute_script(jscommand)
match=False
while(match==False):
    lastCount = lenOfPage
    
    time.sleep(5)
    
    lenOfPage = browser.execute_script(jscommand)
    if lastCount == lenOfPage:
        match=True

time.sleep(5)



followers = []

followers_field = browser.find_elements(By.CSS_SELECTOR, "._ap3a._aaco._aacw._aacx._aad7._aade")

for follower in followers_field:
    followers.append(follower.text)


with open("followers.txt", "w", encoding = "UTF-8") as file:
    for follower in followers:
        file.write(follower + "\n")















#bildirim_button = browser.find_element(By.XPATH, "._a9--._ap36._a9_1")

#send_keys(Keys.RETURN)

#_a9-- _ap36 _a9_1


#browser.find_element(By.CSS_SELECTOR, "._a9-- _ap36 _a9_1").click()

#browser.find_element(By.XPATH,"/html/body/div[3]/div[1]/div/div[2]/div/div/div/div/div[2]/div/div/div[3]/button[2]").click()


#browser.find_element(By.XPATH, "/html/body/div[2]/div/div/div[2]/div/div/div[1]/div[1]/div[1]/div/div/div/div/div[2]/div[8]/div/span/div/a/div/div[2]/div/div/span/span").click()
#searchArea.send_keys(Keys.RETURN)

#browser.quit()



















