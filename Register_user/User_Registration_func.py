from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


driver = Chrome()

def register_user (username,user_email):
   # driver.get("https://automationexercise.com/login")
    name=driver.find_element(by=By.XPATH,value="//input[@placeholder='Name']")
    email=driver.find_element(by=By.XPATH,value = "//input[@data-qa='signup-email']")
    btn_signup=driver.find_element(by=By.XPATH,value = "//button[normalize-space()='Signup']")
    name.send_keys(username)
    email.send_keys(user_email)
    btn_signup.click()

