#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/radio-button")
driver.implicitly_wait(10)


driver.find_element_by_css_selector("div.custom-radio label[for=impressiveRadio]").click()
radioNo = driver.find_element_by_css_selector("div.custom-radio #noRadio").get_attribute("disabled")

assert radioNo == "true"
assert driver.find_element_by_css_selector("div.playgound-body .mt-3").text == "You have selected Impressive"

close_browser(timeout=3)