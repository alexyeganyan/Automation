#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/checkbox")
driver.implicitly_wait(10)


driver.find_element_by_css_selector("div.react-checkbox-tree .rct-icon-expand-all").click()
driver.find_element_by_css_selector("div.react-checkbox-tree label[for=tree-node-angular]").click()

close_browser(timeout=3)