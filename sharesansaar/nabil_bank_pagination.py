import time
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def nabil_pagination(driver):
    search_field = driver.find_element(*(By.XPATH,"//input[@id='company_search']"))
    search_field.send_keys("Nabil")
    time.sleep(1)
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(2)
    scroll_page(driver)
    price_history = driver.find_element(*(By.XPATH, "//a[@id='btn_cpricehistory']"))
    price_history.click()
    time.sleep(1)
    entries = driver.find_element(*(By.XPATH,"//select[@name='myTableCPriceHistory_length']"))
    entries.click()
    actions.send_keys(Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(2)
    scroll_page(driver)
    # time.sleep(1)
    print("Current Page Title:", driver.title)
    while True:
        try:
            next_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@id='myTableCPriceHistory_next']")))
            # Click the "Next" button
            next_button.click()
            time.sleep(0.5)

            # previous_button = WebDriverWait(driver, 10).until(
            # EC.presence_of_element_located((By.XPATH, "//a[@id='myTableCPriceHistory_previous']")))
            # previous_button.click()
            # time.sleep(0.5)
        except:
            break
    while True:
        try:
            previous_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, "//a[@id='myTableCPriceHistory_previous']")))
            previous_button.click()
            time.sleep(0.5)
        except:
            break





