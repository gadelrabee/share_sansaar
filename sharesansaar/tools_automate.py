import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import scroll_page

def tools(driver):
    tools = WebDriverWait(driver,10).until(
    EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Tools']"))
    )
    tools.click()
    share_calcu = WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='Share Calculator']"))
    )
    share_calcu.click()
    time.sleep(2)
    share_quantity = driver.find_element(*(By.XPATH,"//input[@id='share_qty']"))
    share_quantity.clear()
    share_quantity.send_keys("70")
    time.sleep(2)

    purchase_price = driver.find_element(*(By.XPATH,"//input[@id='purchase_price']"))
    purchase_price.clear()
    purchase_price.send_keys("634")
    time.sleep(4)

    clear = driver.find_element(*(By.XPATH,"//button[@id='share-calculate-clear-btn']"))
    clear.click()
    time.sleep(2)
    driver.back()

    emi_calculator = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='EMI Calculator']"))
    )
    emi_calculator.click()
    driver.find_element(*(By.XPATH,"//input[@id='loan_amount']")).send_keys("1500000")
    time.sleep(1)
    driver.find_element(*(By.XPATH,"//input[@id='interest_rate']")).send_keys("15")
    time.sleep(1)
    driver.find_element(*(By.XPATH,"//input[@id='duration']")).send_keys("5")
    time.sleep(1)
    driver.find_element(*(By.XPATH,"//button[@id='emi-calculate-btn']")).click()
    time.sleep(4)
    driver.find_element(*(By.XPATH,"//button[@id='emi-calculate-clear-btn']")).click()
    time.sleep(2)
    driver.back()


