#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/webtables")
driver.implicitly_wait(10)

Select(driver.find_element_by_css_selector("div.ReactTable select[aria-label='rows per page']")).select_by_value("5")
text_edit = "div.ReactTable #edit-record-2"
driver.find_element_by_css_selector(text_edit).click()
first_name = driver.find_element_by_css_selector("#firstName")
first_name.clear()
first_name.send_keys("Adriana")
salary = driver.find_element_by_css_selector("#salary")
salary.clear()
salary.send_keys("14500")
driver.find_element_by_css_selector("#submit").click()


# close_browser(timeout=3)