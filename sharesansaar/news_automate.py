import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import requests

from helper import scroll_page


def news(driver):
    news = WebDriverWait(driver,10).until(
           EC.presence_of_element_located((By.XPATH,"//a[normalize-space()='News']"))).click()
    time.sleep(2)
    all_news = driver.find_element(*(By.XPATH,"//a[normalize-space()='All News']"))
    announcements = driver.find_element(*(By.XPATH,"//a[normalize-space()='Announcements']"))
    driver.save_screenshot("C:\\Users\\rabee\\Desktop\\selenium\\picture2.png")

    # Extract and print the website title
    website_title = driver.title
    print(f"Website Title: {website_title}")

    actions = ActionChains(driver)
    actions.move_to_element(all_news).click().perform()
    scroll_page(driver)

    driver.back()
    actions.move_to_element(all_news).move_to_element(announcements).click().perform()
    time.sleep(3)
    scroll_page(driver)

    # company
    company_symbol = driver.find_element(*(By.XPATH, "//input[@id='company']"))
    company_symbol.clear()
    company_symbol.send_keys("D")
    time.sleep(2)

    # sector
    driver.find_element(*(By.XPATH, "//span[@id='select2-sector-container']")).click()
    driver.find_element(*(By.XPATH, "//body"))
    actions = ActionChains(driver)
    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(3)

    # date
    driver.find_element(*(By.XPATH, "//input[@id='fromdate']")).click()
    time.sleep(2)
    driver.find_element(*(By.XPATH, "//table[@class=' table-condensed']//th[@class='prev'][normalize-space()='«']")).click()
    time.sleep(2)
    driver.find_element(*(By.XPATH, "//td[normalize-space()='14']")).click()
    time.sleep(3)

    # category
    driver.find_element(*(By.XPATH, "//span[@id='select2-category-container']")).click()
    time.sleep(2)
    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(3)

    # search
    search = driver.find_element(*(By.XPATH,"//button[@id='btn_announcement_submit']"))
    search.click()
    time.sleep(2)

    # clear
    clear_button = driver.find_element(*(By.XPATH,"//button[@id='btn_announcement-reset']"))
    clear_button.click()
    time.sleep(2)


    print(driver.title)

