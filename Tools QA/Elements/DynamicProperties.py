#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def close_browser(timeout=0):
    time.sleep(timeout)
    driver.close()


def enable_button(elem):
    return elem.find_element_by_css_selector("div.playgound-body #enableAfter").get_attribute("disabled")


def visible_button(elem):
    return not elem.find_element_by_css_selector("div.playgound-body #visibleAfter").get_attribute("visibility")


driver = webdriver.Firefox()
driver.get("https://demoqa.com/dynamic-properties")
driver.implicitly_wait(10)

print(driver.find_element_by_css_selector("div.playgound-body p").text)
# WebDriverWait(driver, 15).until(lambda x: enable_button(x))
driver.find_element_by_css_selector("div.playgound-body #enableAfter").click()
driver.find_element_by_css_selector("div.playgound-body #visibleAfter").click()
# WebDriverWait(driver, 15).until(lambda x: visible_button(x))
# driver.find_element_by_css_selector("div.playgound-body #visibleAfter").click()

close_browser()