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
signLink = driver.find_element_by_css_selector(".header_user_info , .login")
signLink.click()

# Enter valid email address
emailAddress = driver.find_element_by_css_selector("div.columns-container  #email_create")
# emailAddress.send_keys("aaa@gg.com")
emailAddress.send_keys("bbb@gg.com")
# Click on create account
createAccount = driver.find_element_by_css_selector("button#SubmitCreate")
createAccount.click()
# Check Mr. option
gender = driver.find_element_by_css_selector("div.radio-inline #id_gender1")
gender.click()
# Enter first name
firstName = driver.find_element_by_css_selector("div.account_creation #customer_firstname")
firstName.send_keys("Nocholas")
# Enter last name
lastName = driver.find_element_by_css_selector("div.account_creation #customer_lastname")
lastName.send_keys("Johnson")
# Enter password
password = driver.find_element_by_css_selector("div.account_creation #passwd")
password.send_keys("Johnson")
# Enter date
days = Select(driver.find_element_by_css_selector("div#uniform-days #days"))
days.select_by_visible_text("11  ")
months = Select(driver.find_element_by_css_selector("div#uniform-months #months"))
months.select_by_visible_text("May ")
years = Select(driver.find_element_by_css_selector("div#uniform-years #years"))
years.select_by_visible_text("2001  ")
# # Check "Sign up for newsletter" AND "Recieve special offers"
# newsLetter = driver.find_element_by_css_selector(".//*[@id='newsletter']")
# newsLetter.click()
# specialOffer = driver.find_element_by_css_selector(".//*[@id='optin']")
# specialOffer.click()
# # Enter address details
# # Enter first name
# firstName = driver.find_element_by_css_selector(".//*[@id='firstname']")
# firstName.send_keys("Bernard")
# # Enter last name
# lastName = driver.find_element_by_css_selector(".//*[@id='lastname']")
# lastName.send_keys("Lampard")
# # Enter company name
# company = driver.find_element_by_css_selector(".//*[@id='company']")
# company.send_keys("Foormols")
# # Enter address
# address1 = driver.find_element_by_css_selector(".//*[@id='address1']")
# address1.send_keys("1622 E Ayre Street")
# # Enter address
# address2 = driver.find_element_by_css_selector(".//*[@id='address2']")
# address2.send_keys("Sas1120")
# # Enter city
# city = driver.find_element_by_css_selector(".//*[@id='city']")
# city.send_keys("Honk-Kong")
# # Enter state
# state = Select(driver.find_element_by_css_selector(".//*[@id='id_state']"))
# state.select_by_value("5")
# # Enter zip code
# zipCode = driver.find_element_by_css_selector(".//*[@id='postcode']")
# zipCode.send_keys("15444")
# # Enter country
# country = Select(driver.find_element_by_css_selector(".//*[@id='id_country']"))
# country.select_by_value("21")
# # Enter additional info
# additional = driver.find_element_by_css_selector(".//*[@id='other']")
# additional.send_keys("I am an engineer\nI live in Yerevan")
# # Enter home phone
# homePhone = driver.find_element_by_css_selector(".//*[@id='phone']")
# homePhone.send_keys("+37455997711")
# # Enter home phone
# mobilePhone = driver.find_element_by_css_selector(".//*[@id='phone_mobile']")
# mobilePhone.send_keys("+37455883300")
# # Enter email address for future references
# emailReference = driver.find_element_by_css_selector(".//*[@id='alias']")
# emailReference.send_keys("Mango@ss.com")
# # // Register all data
# # register = driver.find_element_by_css_selector(".//*[@id='submitAccount']")
# # register.click()
#
# # Maximize the Browser window
# # driver.manage().window().maximize()
# #
# # // Get the current page URL and store the value in variable 'str'
# # String str = driver.getCurrentUrl()
# #
# # // Print the value of variable in the console
# # System.out.println("The current URL is " + str)
# # // System.out.println(searchText.getText()

time.sleep(3)
driver.close()
