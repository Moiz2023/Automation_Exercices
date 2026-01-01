from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

def open_home(driver, url):
    driver.get(url)
    try:
        WebDriverWait(driver, 5).until(
            EC.element_to_be_clickable((By.XPATH, "/html/body/div/div[2]/div[2]/div[2]/div[2]/button[1]"))
        ).click()
    except:
        pass
    print("✅ Page d'accueil ouverte")



