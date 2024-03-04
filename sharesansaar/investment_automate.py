import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def investment(driver):
    invest = driver.find_element(*(By.XPATH,"//a[normalize-space()='Investment']"))
    invest.click()
    time.sleep(2)
    investment_overview = driver.find_element(*(By.XPATH,"//a[normalize-space()='Investment Overview']"))
    existing_issues = driver.find_element(*(By.XPATH,"//li[@class='has-sub']//ul//li//a[normalize-space()='Existing Issues']"))
    upcoming_issues = driver.find_element(*(By.XPATH,"//a[normalize-space()='Upcoming Issue']"))
    auction = driver.find_element(*(By.XPATH,"//a[normalize-space()='Auction']"))
    actions = ActionChains(driver)
    actions.move_to_element(investment_overview).move_to_element(existing_issues).move_to_element(upcoming_issues).move_to_element(auction).click().perform()
    time.sleep(2)
    scroll_page(driver)
    time.sleep(2)
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP + Keys.PAGE_UP + Keys.PAGE_UP)
    time.sleep(2)
    driver.back()
    actions.move_to_element(investment_overview).click().perform()
    time.sleep(2)
    view_more = driver.find_element(*(By.XPATH,"//a[@href='https://www.sharesansar.com/existing-issues']"))
    view_more.click()
    time.sleep(2)
    scroll_page(driver)
    time.sleep(1)
    driver.back()










