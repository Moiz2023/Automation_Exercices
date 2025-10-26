from time import sleep

from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from User_Registration_func import register_user
#Navigation to url and verification of the display of sign up form
driver = Chrome()
driver.get("https://automationexercise.com/")
driver.maximize_window()
driver.find_element(by=By.XPATH,value = "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]").click()
page_title = driver.title

print(page_title)

driver.find_element(by=By.XPATH, value ="//a[normalize-space()='Signup / Login']").click()
user_signup = driver.find_element(by=By.XPATH,value="//h2[normalize-space()='New User Signup!']")
if user_signup.is_displayed():
    print("User signup is displayed")
else :
    print("User signup is not displayed")


signup_form = driver.find_element(By.CLASS_NAME, "signup-form")

wait = WebDriverWait(driver, timeout=2)
wait.until(lambda _: signup_form.is_displayed())

#register_user("Moiz","slimimoez@gmail.com")
name=driver.find_element(by=By.XPATH,value="//input[@placeholder='Name']")
email=driver.find_element(by=By.XPATH,value = "//input[@data-qa='signup-email']")
btn_signup=driver.find_element(by=By.XPATH,value = "//button[normalize-space()='Signup']")
name.send_keys("Moez")
email.send_keys("slimimoez@gmail.com"
                "")
btn_signup.click()

sleep(4)

#Account information filling
account_info = driver.find_element(by=By.XPATH,value="//b[normalize-space()='Enter Account Information']")
if account_info.is_displayed():
    print("Account information is displayed")
else :
    print("Account information is not displayed")

gender=driver.find_element(by=By.ID,value = 'id_gender1')
