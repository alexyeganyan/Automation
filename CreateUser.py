#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# Create a instance of Firefox Browser
driver = webdriver.Firefox()

# Open the URL in firefox browser
driver.get("http://automationpractice.com/index.php")
driver.implicitly_wait(10)
# driver.findElement(By.id("core-navigation")
driver.find_element_by_css_selector(".header_user_info , .login").click()

# Enter invalid email address and check error message
emailAddress = driver.find_element_by_css_selector("div.columns-container  #email_create").send_keys("bbb@.g.com")

# Click on create account
driver.find_element_by_css_selector("button#SubmitCreate").click()
# Wait until error text is appeared


def len_inner_text(elem):
    return len(elem.find_element_by_css_selector("#create_account_error.alert.alert-danger").get_attribute("innerText"))


WebDriverWait(driver, 15).until(lambda x: len_inner_text(x) > 0)

inner_text = driver.find_element_by_css_selector("#create_account_error.alert.alert-danger").get_attribute("innerText")
assert inner_text == "Invalid email address."

# Enter valid email address
emailAddress = driver.find_element_by_css_selector("div.columns-container  #email_create")
emailAddress.clear()
emailAddress.send_keys("bbb@gg.com")
# emailAddress.send_keys("aaa@gg.com")
# Click on create account
driver.find_element_by_css_selector("button#SubmitCreate").click()
# Check Mr. option
driver.find_element_by_css_selector("div.radio-inline #id_gender1").click()
# Enter first name
driver.find_element_by_css_selector("div.account_creation #customer_firstname").send_keys("Nocholas")
# Enter last name
driver.find_element_by_css_selector("div.account_creation #customer_lastname").send_keys("Johnson")
# Enter password# Enter password
driver.find_element_by_css_selector("div.account_creation #passwd").send_keys("Johnson")
# Enter date
Select(driver.find_element_by_css_selector("div#uniform-days #days")).select_by_visible_text("11  ")
Select(driver.find_element_by_css_selector("div#uniform-months #months")).select_by_visible_text("May ")
Select(driver.find_element_by_css_selector("div#uniform-years #years")).select_by_visible_text("2001  ")
# Check "Sign up for newsletter" AND "Recieve special offers"
newsLetter = driver.find_element_by_css_selector("#newsletter").click()
driver.find_element_by_css_selector("#optin").click()
# Enter address details
# Enter first name
driver.find_element_by_xpath("//*[@id='firstname']").send_keys("Bernard")
# Enter last name
driver.find_element_by_xpath(".//*[@id='lastname']").send_keys("Lampard")
# Enter company name
driver.find_element_by_css_selector("#company").send_keys("Foormols")
# Enter address
driver.find_element_by_css_selector("#address1").send_keys("1622 E Ayre Street")
# Enter address
driver.find_element_by_css_selector("#address2").send_keys("Sas1120")
# Enter city
driver.find_element_by_css_selector("#city").send_keys("Honk-Kong")
# Enter state
Select(driver.find_element_by_xpath(".//*[@id='id_state']")).select_by_value("5")
# Enter zip code
driver.find_element_by_xpath(".//*[@id='postcode']").send_keys("15444")
# Enter country
Select(driver.find_element_by_css_selector("#id_country")).select_by_value("21")
# Enter additional info
driver.find_element_by_css_selector("#other").send_keys("I am an engineer\nI live in Yerevan")
# Enter home phone
driver.find_element_by_css_selector("#phone").send_keys("+37455997711")
# Enter home phone
driver.find_element_by_css_selector("#phone_mobile").send_keys("+37455883300")
# Enter email address for future references
driver.find_element_by_css_selector("#alias").send_keys("Mango@ss.com")
# # // Register all data
# # register = driver.find_element_by_css_selector(".//*[@id='submitAccount']")
# # register.click()
# #
# # // Get the current page URL and store the value in variable 'str'
# # String str = driver.getCurrentUrl()
# #
# # // Print the value of variable in the console
# # System.out.println("The current URL is " + str)
# # // System.out.println(searchText.getText()
#
time.sleep(3)
driver.close()
