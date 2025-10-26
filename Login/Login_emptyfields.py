from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
import time

from login_func import login_page


driver = Chrome()
login_page(username="",password="",driver=driver)

username_error= driver.find_element(by=By.XPATH , value="//div[@class='orangehrm-login-slot-wrapper']//div[1]//div[1]//span[1]")
password_error = driver.find_element(by=By.XPATH , value="//div[@class='orangehrm-login-form']//div[2]//div[1]//span[1]")


#verification of error message display after clicking on login button
username_error.is_displayed()
password_error.is_displayed()

displayed_message_username = username_error.text
displayed_message_password =password_error.text
message_expected = "Required"


print('the error displayed for the username is : ' , displayed_message_username)

print('the error displayed for the password is : ' , displayed_message_password)

assert displayed_message_username==message_expected
assert displayed_message_password==message_expected




time.sleep(4)
