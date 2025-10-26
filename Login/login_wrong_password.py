import time

from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from login_func import login_page

driver = Chrome()
login_page(username="admin",password="dmin123",driver=driver)


credential_message = driver.find_element(by=By.CSS_SELECTOR, value='.oxd-alert-content.oxd-alert-content--error')
displayed_message = credential_message.text
print("the displayed message in case of invalid username is :" ,displayed_message)
expected_cred_message = "Invalid credentials"

assert displayed_message==expected_cred_message


time.sleep(4)