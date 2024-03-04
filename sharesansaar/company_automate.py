import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def company(driver):
    company = driver.find_element(*(By.XPATH, "//a[normalize-space()='Company']")).click()
    listed_company = driver.find_element(*(By.XPATH, "//a[normalize-space()='Listed Companies']"))
    actions = ActionChains(driver)
    # actions.send_keys(Keys.ARROW_DOWN + Keys.ENTER).perform()
    actions.move_to_element(listed_company).click().perform()
    time.sleep(3)
    drop_button = driver.find_element(*(By.XPATH, "//span[@role='presentation']")).click()
    driver.implicitly_wait(2)
    actions.send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(
        Keys.ARROW_DOWN).send_keys(Keys.ARROW_DOWN).send_keys(Keys.ENTER).perform()
    time.sleep(2)
    search = driver.find_element(*(By.XPATH, "//button[@id='btn_listed_submit']")).click()
    time.sleep(3)
    # scroll_page
    scroll_page(driver)