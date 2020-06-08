#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Create a instance of Firefox Browser
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Open the URL in firefox browser
driver.get("http://automationpractice.com/index.php")
# Maximize the Browser window
driver.maximize_window()
driver.implicitly_wait(10)
# driver.implicitly_wait(10)
TShirt = driver.find_element_by_xpath(".//*[@id='block_top_menu']/ul/li/a[@title='T-shirts']")
TShirt.click()
# Select sort criteria
selectProductSort = Select(driver.find_element_by_xpath(".//*[@id='selectProductSort']"))
selectProductSort.select_by_value("reference:asc")
# Check product's size
size = driver.find_element_by_css_selector("#ul_layered_id_attribute_group_1 input#layered_id_attribute_group_3")
size.click()
# Check product's composition
composition = driver.find_element_by_css_selector("#ul_layered_id_feature_5.col-lg-12 div#uniform-layered_id_feature_5")
composition.click()
# Check product's condition
condition = driver.find_element_by_css_selector("#ul_layered_condition_0 #uniform-layered_condition_new")
condition.click()
# Select price range
priceSlider = driver.find_element_by_css_selector(".layered_price #layered_price_slider")
firstSlider = priceSlider.find_element_by_css_selector("[style='left: 0%;']")
lastSlider = priceSlider.find_element_by_css_selector("[style='left: 100%;']")
firstSliderCoord = firstSlider.location
lastSliderCoord = lastSlider.location
# Obtain X and Y coordinates
x1Coord = firstSliderCoord.get("x")
x2Coord = lastSliderCoord.get("x")
delta = x2Coord - x1Coord
# move sliders from two sides
actions = ActionChains(driver)
actions.move_to_element(firstSlider)
actions.drag_and_drop_by_offset(firstSlider, int(0.2 * delta), 0)
actions.perform()
print(int((-0.15) * delta))
actions.move_to_element(lastSlider)
actions.drag_and_drop_by_offset(lastSlider, int((-0.15) * delta), 0)
actions.perform()

time.sleep(5)
driver.close()
