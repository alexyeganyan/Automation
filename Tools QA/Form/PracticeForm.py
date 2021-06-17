#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support import expected_conditions as EC


def close_browser(timeout=0):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/automation-practice-form")
driver.implicitly_wait(10)

driver.find_element_by_css_selector("div#dateOfBirth-wrapper input#dateOfBirthInput").click()
Select(driver.find_element_by_css_selector("select.react-datepicker__month-select")).select_by_visible_text("July")
Select(driver.find_element_by_css_selector("select.react-datepicker__year-select")).select_by_visible_text("2020")
day = "24"
day_selector = ".react-datepicker__day--0" + day
driver.find_element_by_css_selector(day_selector).click()

close_browser()