from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.webdriver import Chrome
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from login_func import login_page

driver = Chrome()
login_page(username="admin", password="admin123",driver=Chrome())

try:
    WebDriverWait(driver, 10).until(EC.alert_is_present())
    print("Alert is visible")
    alert = driver.switch_to.alert
    alert.accept()
except (ValueError, IOError) as e:
    print("Alert not present")

time.sleep(4)
