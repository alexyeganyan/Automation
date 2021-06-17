#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver import ActionChains


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/buttons")
driver.implicitly_wait(10)

button_double = driver.find_element_by_css_selector("div.playgound-body #doubleClickBtn")
ActionChains(driver).double_click(button_double).perform()
button_right = driver.find_element_by_css_selector("div.playgound-body #rightClickBtn")
ActionChains(driver).context_click(button_right).perform()

close_browser(timeout=3)