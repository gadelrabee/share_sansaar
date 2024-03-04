import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def economy(driver):
    # economy
    driver.find_element(*(By.XPATH,"//a[normalize-space()='Economy']")).click()
    time.sleep(2)
    driver.find_element(*(By.XPATH,"//a[normalize-space()='Capital Expenditure']")).click()
    time.sleep(3)
    driver.find_element(*(By.XPATH,"//span[@role='presentation']")).click()
    actions = ActionChains(driver)
    actions.send_keys((Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)).perform()
    driver.find_element(*(By.XPATH,"//button[@id='btn_capexp_submit']")).click()
    scroll_page(driver)
    driver.back()