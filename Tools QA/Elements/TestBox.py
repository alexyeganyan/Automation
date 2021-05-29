#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/text-box")
driver.implicitly_wait(10)

driver.find_element_by_css_selector("div.text-field-container #userName").send_keys("firstname")
driver.find_element_by_css_selector("div.text-field-container #userEmail").send_keys("firstname@gago.vop")
driver.find_element_by_css_selector("div.text-field-container #currentAddress").send_keys("""firstname
AAA 34, rt
qert lop""")
driver.find_element_by_css_selector("div.text-field-container #permanentAddress").send_keys("""firstname
Fart 34, rt
Lookjuy lop""")

close_browser(timeout=3)