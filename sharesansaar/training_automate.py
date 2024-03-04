import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from helper import scroll_page
import pdb

def training(driver):
    training = driver.find_element(*(By.XPATH,"//a[normalize-space()='Training']")).click()
    time.sleep(2)
    indepth_training = driver.find_element(*(By.XPATH,"//a[normalize-space()='Indepth Training']"))
    technical_analysis = driver.find_element(*(By.XPATH,"//a[@href='/technical-analysis-training']"))
    registration_form = driver.find_element(*(By.XPATH,"//a[normalize-space()='Registration Form']"))
    actions = ActionChains(driver)
    actions.move_to_element(indepth_training).click().perform()
    time.sleep(2)
    driver.execute_script("document.body.style.zoom = '1.5';")
    time.sleep(2)
    driver.execute_script("document.body.style.zoom = '1';")
    time.sleep(2)
    driver.execute_script("document.body.style.zoom = '0.3';")
    time.sleep(2)
    driver.back()
    actions.move_to_element(indepth_training).move_to_element(technical_analysis).click().perform()
    scroll_page(driver)
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(1)
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_UP)
    time.sleep(2)
    driver.back()
    actions.move_to_element(indepth_training).move_to_element(technical_analysis).move_to_element(registration_form).click().perform()
    time.sleep(2)
    scroll_page(driver)
    training_program = driver.find_element(*(By.XPATH,"//span[@id='select2-program-container']")).click()
    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(2)

    full_name = driver.find_element(*(By.XPATH,"//input[@id='name']"))
    full_name.clear()
    full_name.send_keys("Gaurav Shrestha")
    time.sleep(1)

    email = driver.find_element(*(By.XPATH,"//input[@id='email']"))
    email.clear()
    email.send_keys("abcdef..124@@gmail.com")
    time.sleep(1)

    mobile = driver.find_element(*(By.XPATH,"//input[@id='mobile_no']"))
    mobile.clear()
    mobile.send_keys("12345678912345")
    time.sleep(1)

    occupation = driver.find_element(*(By.XPATH,"//input[@id='occupation']"))
    occupation.clear()
    occupation.send_keys("Software Tester")
    time.sleep(1)

    age = driver.find_element(*(By.XPATH,"//input[@id='age']"))
    age.clear()
    age.send_keys("4562")
    time.sleep(1)

    address = driver.find_element(*(By.XPATH,"//input[@id='address']"))
    address.clear()
    address.send_keys("lalitpur--8")
    time.sleep(1)

    location = driver.find_element(*(By.XPATH,"//span[@id='select2-location-container']"))
    location.click()
    time.sleep(1)
    actions.send_keys(Keys.ARROW_DOWN + Keys.ARROW_DOWN + Keys.ENTER).perform()
    time.sleep(1)

    any_other = driver.find_element(*(By.XPATH,"//input[@id='other']"))
    any_other.clear()
    any_other.send_keys("Your code has run succesfully.")
    time.sleep(1)

    message = driver.find_element(*(By.XPATH,"//textarea[@id='message']"))
    message.clear()
    message.send_keys("Process finished with exit code 0.")
    time.sleep(1)
    driver.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.PAGE_DOWN)


    # recaptcha = driver.find_element(*(By.XPATH,"//div[@class='recaptcha-checkbox-border']"))
    # recaptcha.click()
    # time.sleep(1)

    submit = driver.find_element(*(By.XPATH,"//button[@type='submit']"))
    submit.click()
    time.sleep(1)

    reset = driver.find_element(*(By.XPATH,"//button[@type='reset']"))
    reset.click()
    time.sleep(5)




