import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def ipo_fpo(driver):
    ipo_fpo = driver.find_element(*(By.XPATH,
                                    "//body/div[@xclass='container-fluid']/div[@xclass='row']/section[@class='main-nav']/div[@class='container']/div[@class='col-md-12']/div[@id='cssmenu']/ul/li[5]/a[1]")).click()
    check_ipo_fpo_result = driver.find_element(*(By.XPATH, "//a[normalize-space()='Check IPO/FPO Result']"))
    ipo_fpo_news = driver.find_element(*(By.XPATH, "//li[5]//ul[1]//li[2]//a[1]"))
    allotment_news = driver.find_element(*(By.XPATH, "//a[normalize-space()='IPO/FPO Allotment News']"))
    actions = ActionChains(driver)
    actions.move_to_element(check_ipo_fpo_result).click().perform()
    time.sleep(2)
    name = driver.find_element(*(By.XPATH, "//span[@id='select2-companyid-container']")).click()
    actions.send_keys(
        Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(2)
    boid_no = driver.find_element(*(By.XPATH, "//input[@id='boid']"))
    boid_no.clear()
    boid_no.send_keys("123456")
    time.sleep(2)
    search = driver.find_element(*(By.XPATH, "//button[@id='searchipo']")).click()
    time.sleep(3)
    clear = driver.find_element(*(By.XPATH, "//button[normalize-space()='Clear']")).click()
    time.sleep(2)
    driver.back()
    actions.move_to_element(check_ipo_fpo_result).move_to_element(ipo_fpo_news).move_to_element(
        allotment_news).click().perform()
    time.sleep(2)
    scroll_page(driver)
    next1 = driver.find_element(*(By.XPATH, "//a[normalize-space()='Next »']")).click()
    time.sleep(3)
    prev = driver.find_element(*(By.XPATH, "//a[normalize-space()='« Previous']")).click()
    time.sleep(2)
    symbol = driver.find_element(*(By.XPATH, "//input[@id='company']"))
    symbol.clear()
    symbol.send_keys("Nabil12")
    time.sleep(2)
    date = driver.find_element(*(By.XPATH, "//input[@id='fromdate']")).click()
    time.sleep(2)
    month = driver.find_element(
        *(By.XPATH, "//table[@class=' table-condensed']//th[@class='prev'][normalize-space()='«']")).click()
    time.sleep(2)
    day = driver.find_element(*(By.XPATH, "//td[@class='day'][normalize-space()='9']")).click()
    time.sleep(2)
    search_button = driver.find_element(*(By.XPATH, "//button[@id='btn_news_submit']")).click()
    time.sleep(2)
    clear = driver.find_element(*(By.XPATH, "//button[@id='btn_news-reset']")).click()
    time.sleep(2)
    driver.back()