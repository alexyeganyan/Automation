#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
import requests


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Chrome()
# driver = webdriver.Firefox()
driver.get("https://demoqa.com/broken")
driver.implicitly_wait(10)


ImageFile = driver.find_element_by_css_selector("div.playgound-body img[src*=Toolsqa_1]")
complete = ImageFile.get_attribute("complete")
width = ImageFile.get_attribute("naturalWidth")
assert (complete == "true") & (int(width) == 0)
broken_link = driver.find_element_by_css_selector("div.playgound-body a[href*=status]")
href = broken_link.get_attribute("href")
assert requests.get(href).status_code != 200
broken_link.click()

close_browser(timeout=3)