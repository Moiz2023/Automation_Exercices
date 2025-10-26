from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait


def wait_Signup_form(driver):
    driver.get('https://automationexercise.com/')
    signup_form = driver.find_element(By.CLASS_NAME, "signup-form")
    driver.find_element(By.ID, "reveal").click()

    wait = WebDriverWait(driver, timeout=2)
    wait.until(lambda _ : signup_form.is_displayed())



