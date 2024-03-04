import time
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys


def scroll_page(driver):
    # scroll_page
    page_height = driver.execute_script("return document.body.scrollHeight")
    scroll_speed = 200
    scroll_iterations = int(page_height / scroll_speed)
    for _ in range(scroll_iterations):
        driver.execute_script(f"window.scrollBy(0, {scroll_speed});")
        time.sleep(0.1)
    time.sleep(2)
