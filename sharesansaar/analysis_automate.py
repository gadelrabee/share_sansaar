import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page

def analysis(driver):
    analysis = WebDriverWait(driver, 10).until(
               EC.element_to_be_clickable((By.XPATH, "//a[normalize-space()='Analysis']"))
                )
    analysis.click()
    time.sleep(2)
    technical_analysis = driver.find_element(*(By.XPATH, "//body/div[@xclass='container-fluid']/div[@xclass='row']/section[@class='main-nav']/div[@class='container']/div[@class='col-md-12']/div[@id='cssmenu']/ul/li[11]/ul[1]/li[1]/a[1]"))
    moving_average = driver.find_element(*(By.XPATH, "//li[@class='has-sub']//ul//li//a[normalize-space()='Moving Average']"))
    days_average = driver.find_element(*(By.XPATH, "//a[normalize-space()='180-Days Average']"))
    pivot_analysis = driver.find_element(*(By.XPATH, "//li[@class='has-sub']//ul//li//a[normalize-space()='Pivot Analysis']"))
    top_companies = driver.find_element(*(By.XPATH, "//a[@href='/top-companies-in-nepal']"))
    actions = ActionChains(driver)
    actions.move_to_element(technical_analysis).move_to_element(moving_average).move_to_element(days_average).click().perform()
    time.sleep(2)
    select_sector = driver.find_element(*(By.XPATH, "//span[@role='combobox']")).click()
    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(2)
    scroll_page(driver)
    driver.find_element(by=By.TAG_NAME, value="Body").send_keys(Keys.PAGE_UP + Keys.PAGE_UP + Keys.PAGE_UP)
    show = driver.find_element(*(By.XPATH, "//select[@name='myTable_length']")).click()
    time.sleep(1)
    actions.send_keys(Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(1)
    search = driver.find_element(*(By.XPATH, "//button[@id='btn_180days_submit']"))
    search.click()

    time.sleep(5)
    driver.back()
    actions.move_to_element(technical_analysis).move_to_element(moving_average).move_to_element(days_average).move_to_element(pivot_analysis).move_to_element(top_companies).click().perform()
    time.sleep(2)
    scroll_page(driver)




