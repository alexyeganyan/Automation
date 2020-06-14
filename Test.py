#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
# Step 1) Open Firefox
# browser = webdriver.Chrome()
browser = webdriver.Firefox()
# Step 2) Navigate to Facebook
browser.get("http://www.facebook.com")
# Add cookies to sign in with the user
browser.add_cookie({'name': 'c_user', 'value': '100001829131180'})
browser.add_cookie({'name': 'xs', 'value': '17%3AQ_NNMgaNa3F5Gw%3A2%3A1592077663%3A12249%3A3687'})
# Reload page to open it with with the signed information cookies
browser.get("http://www.facebook.com")

page_title = browser.title
assert page_title == "Facebook"

time.sleep(5)
browser.close()
