import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from helper import scroll_page

def ss_pro(driver):
    WebDriverWait(driver,10).until(
        EC.presence_of_element_located((By.XPATH,"//a[contains(text(),'⬈ SS Pro')]"))).click()
    time.sleep(2)
    ss_pro_login = driver.find_element(*(By.XPATH, "//a[normalize-space()='Login to SS Pro']"))
    about_sspro = driver.find_element(*(By.XPATH,"//a[normalize-space()='About SS Pro']"))
    actions = ActionChains(driver)

    actions.move_to_element(ss_pro_login).click().perform()
    time.sleep(2)
    driver.back()


    actions.move_to_element(ss_pro_login).move_to_element(about_sspro).click().perform()
    time.sleep(2)
    scroll_page(driver)
    time.sleep(4)
    driver.back()
