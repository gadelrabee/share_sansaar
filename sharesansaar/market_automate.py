import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def market(driver):
    # market
    driver.find_element(*(By.XPATH, "//a[normalize-space()='Market']")).click()
    market_overview = driver.find_element(*(By.XPATH, "//a[normalize-space()='Market Overview']"))
    live_trading = driver.find_element(*(By.XPATH, "//a[normalize-space()='Live Trading']"))
    stock_heat = driver.find_element(*(By.XPATH, "//a[normalize-space()='Stock Heat Map']"))
    todays_share_price = driver.find_element(
        *(By.XPATH, "//li[@class='has-sub']//ul//li//a[@href='/today-share-price']"))
    floorsheet = driver.find_element(*(By.XPATH, "//li[@class='has-sub']//ul//li//a[normalize-space()='Floorsheet']"))
    actions = ActionChains(driver)
    actions.move_to_element(market_overview).move_to_element(live_trading).move_to_element(stock_heat).click().perform()
    time.sleep(2)
    by_volume = driver.find_element(*(By.XPATH,"//a[normalize-space()='By Volume']")).click()
    time.sleep(3)
    fullscreen = driver.find_element(*(By.XPATH, "//button[@id='fullscreen']")).click()
    time.sleep(2)
    refresh = driver.find_element(*(By.XPATH, "//button[@id='refresh']")).click()
    time.sleep(2)
    driver.back()

    actions.move_to_element(market_overview).move_to_element(live_trading).move_to_element(stock_heat).move_to_element(
        todays_share_price).move_to_element(floorsheet).click().perform()
    select_company = driver.find_element(*(By.XPATH, "//span[@role='presentation']")).click()
    time.sleep(2)
    actions.send_keys((Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER)).perform()
    time.sleep(1)
    date = driver.find_element(*(By.XPATH, "//input[@id='date']")).click()
    time.sleep(1)
    back1 = driver.find_element(
        *(By.XPATH, "//div[@class='datepicker-days']//th[@class='prev'][normalize-space()='«']")).click()
    time.sleep(1)
    back2 = driver.find_element(
        *(By.XPATH, "//div[@class='datepicker-days']//th[@class='prev'][normalize-space()='«']")).click()
    time.sleep(1)
    day = driver.find_element(*(By.XPATH, "//td[normalize-space()='18']")).click()
    time.sleep(2)
    buyer_broker = driver.find_element(*(By.XPATH, "//input[@id='buyer']"))
    buyer_broker.clear()
    buyer_broker.send_keys("Pritam Waiba")
    time.sleep(2)
    seller_broker = driver.find_element(*(By.XPATH, "//input[@id='seller']"))
    seller_broker.clear()
    seller_broker.send_keys("Gaurav Shrestha")
    time.sleep(2)
    search = driver.find_element(*(By.XPATH, "//button[@id='btn_flsheet_submit']")).click()
    time.sleep(3)
    driver.back()