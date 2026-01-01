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
    driver.find_element(by=By.XPATH, value="//input[@placeholder='Password']").send_keys("slimi")
    driver.find_element(by=By.XPATH,value="//button[normalize-space()='Login']").click()
    login_success = wait.until(EC.visibility_of_element_located((By.XPATH,"//li[10]//a[1]")))
    print(login_success)
    if login_success.is_displayed():
        print("🎉 Login success  !'Logged as Moez' is displayed.")
    else:
        print("❌ Message not displayed")
    driver.find_element(by=By.XPATH, value="//a[normalize-space()='Logout']").click()
    logout_validation=driver.find_element(by=By.XPATH, value="//h2[normalize-space()='Login to your account']")
    if logout_validation.is_displayed():
        print("🎉User is logged out and navigated to login page")
    else :
        print("logout button not successfully clicked")




finally:
    driver.quit()