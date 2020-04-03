#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Create a instance of Firefox Browser
driver = webdriver.Firefox()

# Open the URL in firefox browser
driver.get("http://automationpractice.com/index.php")
# driver.implicitly_wait(10)
# TShirt = driver.find_element_by_css_selector(".sf-menu > li:nth-child(3) > a:nth-child(1)")
TShirt = driver.find_element().by
# TShirt = driver.find_element_by_xpath("/html/body/div/div[1]/header/div[3]/div/div/div[6]/ul/li[3]/a")
# TShirt = driver.find_element_by_xpath(".//*[@title='T-shirts']")
TShirt.click()
# Select sort criteria
selectProductSort = Select(driver.find_element_by_xpath(".//*[@id='selectProductSort']"))
selectProductSort.select_by_value("reference:asc")
#selectProductSort
#selectProductSort > option:nth-child(7)