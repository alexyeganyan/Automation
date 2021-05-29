#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait

# Step 1) Open Firefox
# driver = webdriver.Chrome()
driver = webdriver.Firefox()
# Step 2) Navigate to Facebook
driver.get("https://platform.activestate.com")
# Add cookies to sign in with the user
driver.add_cookie()
driver.add_cookie()
# driver.add_cookie({'name': 'c_user', 'value': '100001829131180'})
# driver.add_cookie({'name': 'xs', 'value': '17%3AQ_NNMgaNa3F5Gw%3A2%3A1592077663%3A12249%3A3687'})
# Reload page to open it with the signed information cookies
driver.get("https://platform.activestate.com")

time.sleep(5)
driver.close()
