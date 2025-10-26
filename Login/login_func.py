#import selenium
#from selenium import webdriver
import time
from selenium.webdriver.support import expected_conditions as EC

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def login_page(username,password,driver):
   # driver = Chrome()
    driver.get(url='https://opensource-demo.orangehrmlive.com')
    page_title = driver.title
    print('the page title is' ,page_title)
    time.sleep(3)
    username_element = driver.find_element(by=By.NAME , value="username")
    username_element.send_keys(username)

    password_element = driver.find_element(by=By.NAME, value="password")
    password_element.send_keys(password)

    login_btn = driver.find_element(by=By.TAG_NAME , value="button")
    login_btn.click()
    time.sleep(4)

#login_page(username="admin",password="admin123")
# try:
#     WebDriverWait(driver, 10).until(EC.alert_is_present())
#     print("Alerte visible")
#     alert = driver.switch_to.alert
#     alert.accept()
# except:
#     print("Alerte non présente")
#
#




