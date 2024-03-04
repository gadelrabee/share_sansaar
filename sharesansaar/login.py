import time
from selenium.webdriver.common.by import By


def user_login(driver):
    driver.find_element(*(By.XPATH,"//a[normalize-space()='Login']")).click()
    driver.implicitly_wait(10)
    driver.find_element(*(By.XPATH,"//input[@id='email']")).send_keys("rabeegadel5@gmail.com")
    time.sleep(3)
    driver.find_element(*(By.XPATH,"//input[@id='password']")).send_keys("abcde@1234")
    time.sleep(2)
    driver.find_element(*(By.XPATH,"//label[normalize-space()='Remember Me']")).click()
    time.sleep(2)
    driver.find_element(*(By.XPATH,"//input[@value='Login']")).click()
    time.sleep(2)
    driver.find_element(*(By.XPATH,"//div[@id='cssmenu']//a[normalize-space()='Home']")).click()
    time.sleep(5)