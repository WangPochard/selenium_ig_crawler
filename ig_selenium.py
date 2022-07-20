import time
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import os
import wget

path = "E:/crawler/chromedriver/chromedriver.exe"
driver = webdriver.Chrome(path)
driver.get("https://www.instagram.com/")

username = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "username"))
)
password = WebDriverWait(driver, 10).until(
    EC.presence_of_element_located((By.NAME, "password"))
)
login = driver.find_element_by_xpath('//*[@id="loginForm"]/div/div[3]')

username.clear()
password.clear()
username.send_keys('abcd@gmail.com')  #輸入ig帳號
password.send_keys('abcd')  #輸入ig密碼

login.click()

search = WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.XPATH, '//*[@id="react-root"]/section/nav/div[2]/div/div/div[2]/input'))
)
keyword = "#frenchie"
search.send_keys(keyword)
time.sleep(1)
link = driver.find_element_by_class_name("-qQT3")
link.click()
time.sleep(1)

WebDriverWait(driver, 20).until(
    EC.presence_of_element_located((By.CLASS_NAME, '_aagt'))
)
imgs = driver.find_elements_by_class_name("_aagt")

path_dir = "E:/crawler/frenchie"
os.mkdir(path_dir)
print(path_dir)
count = 0
for img in imgs:
    save_as = os.path.join(path_dir, "frenchie_" + str(count) + ".jpg")
    print(img.get_attribute("src"))
    wget.download(img.get_attribute("src"), save_as)
    count += 1

