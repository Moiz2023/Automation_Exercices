from time import sleep


from select import select
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import Select

from driver_setup import get_driver
from Open_website import open_home
from go_to_signup import go_to_signup_form
from account_form import fill_account_form

driver=get_driver()

user_data = {
"password": "slimi",
    "day": "26",
    "month": "May",
    "year": "1988",
    "first_name": "Moez",
    "last_name": "Slimi",
    "address": "koningin astridlaan 56",
    "country": "New Zealand",
    "state": "oost vlaanderen",
    "city": "wetteren",
    "zipcode": "9230",
    "mobile": "0470173175"
}
try:
    open_home(driver,"https://automationexercise.com/")
    go_to_signup_form(driver,"Moez","slimimoez@gmail.com")
    fill_account_form(driver,user_data)
    driver.find_element(by=By.XPATH,value="//a[normalize-space()='Continue']").click()
    driver.find_element(by=By.XPATH, value="//a[normalize-space()='Delete Account']").click()
    wait = WebDriverWait(driver, 10)
    delete_msg = wait.until(EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Account Deleted!']")))
    if delete_msg.is_displayed():
        print("🎉 Account deleted successfully ! the message 'ACCOUNT DELETED' is displayed.")
    else:
        print("❌ Message not displayed")

finally:
    driver.quit()






















