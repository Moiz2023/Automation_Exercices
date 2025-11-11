
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def go_to_signup_form(driver,name,email):
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    WebDriverWait(driver, 5).until(
        EC.visibility_of_element_located((By.XPATH, "//h2[normalize-space()='New User Signup!']"))
    )
    print("✅ Formulaire d'inscription affiché")
    name_element = driver.find_element(by=By.XPATH, value="//input[@placeholder='Name']")
    email_element = driver.find_element(by=By.XPATH, value="//input[@data-qa='signup-email']")
    btn_signup = driver.find_element(by=By.XPATH, value="//button[normalize-space()='Signup']")
    name_element.send_keys(name)
    email_element.send_keys(email)
    btn_signup.click()