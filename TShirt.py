#!/usr/bin/env python3
import time

from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select


def open_browser(url, browser):
    global driver
    # Create a instance of Browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    # Open the URL in the browser
    driver.get(url)
    driver.maximize_window()
    driver.implicitly_wait(10)


def click_tshirt_sort():
    # Click on T-shirts' link
    driver.find_element_by_xpath(".//*[@id='block_top_menu']/ul/li/a[@title='T-shirts']").click()
    # Select sort criteria
    Select(driver.find_element_by_css_selector("#productsSortForm #selectProductSort")).select_by_value("reference:asc")


def product_size_composition_condition():
    # Check product's size
    driver.find_element_by_css_selector("#ul_layered_id_attribute_group_1 input#layered_id_attribute_group_3").click()
    # Check product's composition
    driver.find_element_by_css_selector("#ul_layered_id_feature_5.col-lg-12 div#uniform-layered_id_feature_5").click()
    # Check product's condition
    driver.find_element_by_css_selector("#ul_layered_condition_0 #uniform-layered_condition_new").click()
    # Select price range


def change_price_range_with_slider():
    global actions
    if driver.name == "chrome":
        price_slider = driver.find_element_by_css_selector(".layered_price #layered_price_slider")
        first_slider = price_slider.find_element_by_css_selector("[style='left: 0%;']")
        last_slider = price_slider.find_element_by_css_selector("[style='left: 100%;']")
        first_slider_coord = first_slider.location
        last_slider_coord = last_slider.location
        print(first_slider_coord)
        print(last_slider_coord)
        # Obtain X and Y coordinates
        x1_coord = first_slider_coord.get("x")
        x2_coord = last_slider_coord.get("x")
        delta = x2_coord - x1_coord
        # move sliders from two sides
        actions = ActionChains(driver)
        actions.move_to_element(first_slider)
        actions.drag_and_drop_by_offset(first_slider, int(0.2 * delta), 0)
        actions.perform()
        actions.move_to_element(last_slider)
        actions.drag_and_drop_by_offset(last_slider, int((-0.15) * delta), 0)
        actions.perform()


def open_wearing_name():
    global actions
    # Open a wearing with the certain name
    if driver.name == "chrome":
        # Add to cart a wearing with the certain name
        wearing = driver.find_element_by_css_selector(
            ".product-container a.product-name[title='Faded Short Sleeve T-shirts']")
        actions = ActionChains(driver)
        actions.move_to_element(wearing)
        actions.perform()
        cart = driver.find_element_by_css_selector(
            ".product-container .ajax_add_to_cart_button.btn[title='Add to cart']")
        cart.click()
        # Proceed to checkout
        checkout = driver.find_element_by_css_selector("#layer_cart .clearfix a[title='Proceed to checkout']")
        checkout.click()


def close_browser():
    time.sleep(3)
    driver.close()


open_browser(url="http://automationpractice.com/index.php", browser="chrome")
click_tshirt_sort()
product_size_composition_condition()
change_price_range_with_slider()
open_wearing_name()
close_browser()
