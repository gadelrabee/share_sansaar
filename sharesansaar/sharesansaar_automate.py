import re
import pdb
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.service import Service as ChromeService
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from bs4 import BeautifulSoup

# custom imports
from helper import scroll_page
from login import user_login
from news_automate import news
from economy_automate import economy
from market_automate import market
from IPO_FPO_automate import ipo_fpo
from company_automate import company
from investment_automate import investment
from training_automate import training
from knowledge_automate import knowledge
from analysis_automate import analysis
from tools_automate import tools
from ss_pro_automation import ss_pro
from nabil_bank_pagination import nabil_pagination



driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))

def is_valid_email(email):
    try:
        email_pattern = "^[a-z]+[\._]?[a-z 0-9]+[@]\w+[.]\w{2,3}$"
        if re.search(email_pattern,email):
            return True
        else:
            return False
    except Exception as e:
        print(e)
    return False

def is_valid_mobile(mobile):
    return bool(re.match(r'^\d{10}$', mobile))

driver.get("https://www.sharesansar.com")
driver.maximize_window()
time.sleep(2)
scroll_page(driver)

# login
user_login(driver)

# news_automate
news(driver)
driver.save_screenshot("C:\\Users\\rabee\\Desktop\\selenium\\picture.png")

# economy_automate
economy(driver)

# market_automate
market(driver)

# IPO/FPO
ipo_fpo(driver)

# company
company(driver)

# investment
investment(driver)

# training_automation
training(driver)

# knowledge_automatiom
knowledge(driver)

# analysis_automate
analysis(driver)

# tools_automation
tools(driver)

# ss_pro_automation
ss_pro(driver)


# nabil_pagination
nabil_pagination(driver)



driver.quit()
print("Your code has run successfully.")


