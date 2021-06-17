#!/usr/bin/env python3

import time
from selenium import webdriver


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


driver = webdriver.Firefox()
driver.get("https://demoqa.com/upload-download")
driver.implicitly_wait(10)


uploadFile = driver.find_element_by_css_selector("div.form-file #uploadFile")
uploadFile.send_keys("C:\\Users\\Alex\\Desktop\\aaa.pdf")

close_browser(timeout=3)