from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait, Select
from selenium.webdriver.support import expected_conditions as EC

def fill_account_form(driver, user_data):
    wait = WebDriverWait(driver, 10)
    wait.until(EC.visibility_of_element_located((By.XPATH, "//b[normalize-space()='Enter Account Information']")))
    print("✅ Page 'Enter Account Information' affichée")
    driver.find_element(by=By.ID, value='id_gender1').click()

    driver.find_element(by=By.ID, value='password').send_keys(user_data["password"])

    Select(driver.find_element(by=By.ID, value='days')).select_by_visible_text(user_data["day"])
    Select(driver.find_element(by=By.ID, value='months')).select_by_visible_text(user_data["month"])
    Select(driver.find_element(by=By.ID, value='years')).select_by_visible_text(user_data["year"])

    driver.find_element(by=By.ID, value='newsletter').click()

    driver.find_element(by=By.ID, value='optin').click()

    driver.find_element(by=By.ID, value='first_name').send_keys(user_data["first_name"])

    driver.find_element(by=By.ID, value='last_name').send_keys(user_data["last_name"])

    driver.find_element(by=By.ID, value='address1').send_keys(user_data["address"])

    Select(driver.find_element(by=By.ID, value='country')).select_by_visible_text(user_data["country"])

    driver.find_element(by=By.ID, value='state').send_keys(user_data["state"])

    driver.find_element(by=By.ID, value='city').send_keys(user_data["city"])

    driver.find_element(by=By.ID, value='zipcode').send_keys(user_data["zipcode"])

    driver.find_element(by=By.ID, value='mobile_number').send_keys(user_data["mobile"])

    driver.find_element(by=By.XPATH, value="//button[normalize-space()='Create Account']").click()

