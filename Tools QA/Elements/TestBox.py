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
driver.find_element_by_css_selector("div.text-field-container #userEmail").send_keys("firstnamegago.vop")
driver.find_element_by_css_selector("div.text-field-container #currentAddress").send_keys("""firstname
AAA 34, rt
qert lop""")
driver.find_element_by_css_selector("div.text-field-container #permanentAddress").send_keys("""firstname
Fart 34, rt
Lookjuy lop""")
# driver.find_element_by_css_selector("div.text-field-container #submit").click()
#html body div#app div.body-height div.container.playgound-body div.row div.col-12.mt-4.col-md-6 div.check-box-tree-wrapper div#tree-node.react-checkbox-tree.rct-icons-fa4 ol li.rct-node.rct-node-parent.rct-node-expanded ol li.rct-node.rct-node-parent.rct-node-expanded span.rct-text button.rct-collapse.rct-collapse-btn svg.rct-icon.rct-icon-expand-open path
# close_browser(timeout=3)