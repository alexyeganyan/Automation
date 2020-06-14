#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select

# Create a instance of Firefox Browser
# driver = webdriver.Firefox()
driver = webdriver.Chrome()

# Open the URL in the browser
driver.get("http://automationpractice.com/index.php")
# Maximize the browser window
driver.maximize_window()
driver.implicitly_wait(10)
# Click on T-shirts' link
TShirt = driver.find_element_by_xpath(".//*[@id='block_top_menu']/ul/li/a[@title='T-shirts']")
TShirt.click()
# Select sort criteria
selectProductSort = Select(driver.find_element_by_css_selector("#productsSortForm #selectProductSort"))
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
print(driver.name)
if driver.name == "chrome":
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
    actions.move_to_element(lastSlider)
    actions.drag_and_drop_by_offset(lastSlider, int((-0.15) * delta), 0)
    actions.perform()

# # Open a wearing with the certain name
# wearing = driver.find_element_by_css_selector(".product-container a.product-name[title='Faded Short Sleeve T-shirts']")
# wearing.click()
if driver.name == "chrome":
    # Add to cart a wearing with the certain name
    wearing = driver.find_element_by_css_selector(".product-container a.product-name[title='Faded Short Sleeve T-shirts']")
    actions = ActionChains(driver)
    actions.move_to_element(wearing)
    actions.perform()
    cart = driver.find_element_by_css_selector(".product-container .ajax_add_to_cart_button.btn[title='Add to cart']")
    cart.click()
    # Proceed to checkout
    checkout = driver.find_element_by_css_selector("#layer_cart .clearfix a[title='Proceed to checkout']")
    checkout.click()

time.sleep(5)
driver.close()
