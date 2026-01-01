from TestCase1_Register_user.Open_website import open_home
from TestCase1_Register_user.driver_setup import get_driver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
driver = get_driver()
wait = WebDriverWait(driver, 10)
try:
    open_home(driver,"https://automationexercise.com/")
    driver.find_element(by=By.XPATH,value="//section[@id='slider']//div[@class='item active']//div[1]").is_displayed()
    driver.find_element(By.LINK_TEXT, "Signup / Login").click()
    driver.find_element(by=By.XPATH, value="//h2[normalize-space()='Login to your account']").is_displayed()
    driver.find_element(by=By.XPATH,value="//input[@data-qa='login-email']").send_keys("slimimoez@gmail.com")
    driver.find_element(by=By.XPATH, value="//input[@placeholder='Password']").send_keys("slimim")
    driver.find_element(by=By.XPATH,value="//button[normalize-space()='Login']").click()
    login_failed = wait.until(EC.visibility_of_element_located((By.XPATH,"//p[normalize-space()='Your email or password is incorrect!']")))
    print(login_failed)
    if login_failed.is_displayed():
        print("❌ Login failed  !'Your email or password is incorrect!' is displayed.")
    else:
        print("Message not displayed")


finally:
    driver.quit()