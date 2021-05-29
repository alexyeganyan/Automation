#!/usr/bin/env python3

from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
import time

# driver = webdriver.Remote(command_executor="http://192.168.0.108:4444/wd/hub",
#                           desired_capabilities={"browserName": "firefox"})


def enter_email_address(address):
    email_address = driver.find_element_by_css_selector("div.columns-container  #email_create")
    email_address.clear()
    email_address.send_keys(address)
    # Click on create account
    driver.find_element_by_css_selector("button#SubmitCreate").click()


def enter_name_password_gender(firstname, lastname, password):
    # Check Mr. option
    driver.find_element_by_css_selector("div.radio-inline #id_gender1").click()
    # Enter first name
    driver.find_element_by_css_selector("div.account_creation #customer_firstname").send_keys(firstname)
    # Enter last name
    driver.find_element_by_css_selector("div.account_creation #customer_lastname").send_keys(lastname)
    # Enter password
    driver.find_element_by_css_selector("div.account_creation #passwd").send_keys(password)


def enter_date(day, month, year):
    Select(driver.find_element_by_css_selector("div#uniform-days #days")).select_by_visible_text(day)
    Select(driver.find_element_by_css_selector("div#uniform-months #months")).select_by_visible_text(month)
    Select(driver.find_element_by_css_selector("div#uniform-years #years")).select_by_visible_text(year)


def valid_inner_text(elem):
    return elem.find_element_by_css_selector("#create_account_error.alert.alert-danger").get_attribute("innerText")


def check_error_text():
    # Wait until error text is appeared
    WebDriverWait(driver, 15).until(lambda x: valid_inner_text(x))
    inner_text = driver.find_element_by_css_selector("#create_account_error.alert.alert-danger").get_attribute(
        "innerText")
    assert inner_text == "Invalid email address."


def open_browser(url, browser):
    global driver
    # Create a instance of Browser
    if browser == "chrome":
        driver = webdriver.Chrome()
    elif browser == "firefox":
        driver = webdriver.Firefox()
    # Open the URL in the browser
    driver.get(url)
    driver.implicitly_wait(10)
    driver.find_element_by_css_selector(".header_user_info , .login").click()


def enter_firstname_lastname_company(first_name, last_name, company):
    # Enter first name
    driver.find_element_by_xpath("//*[@id='firstname']").send_keys(first_name)
    # Enter last name
    driver.find_element_by_xpath(".//*[@id='lastname']").send_keys(last_name)
    # Enter company name
    driver.find_element_by_css_selector("#company").send_keys(company)


def enter_addresses_city_state(address, address2, city, state):
    # Enter address
    driver.find_element_by_css_selector("#address1").send_keys(address)
    # Enter address 2
    driver.find_element_by_css_selector("#address2").send_keys(address2)
    # Enter city
    driver.find_element_by_css_selector("#city").send_keys(city)
    # Enter state
    Select(driver.find_element_by_xpath(".//*[@id='id_state']")).select_by_visible_text(state)


def enter_zip_country_info(zip_code, country, additional_info):
    # Enter zip code
    driver.find_element_by_xpath(".//*[@id='postcode']").send_keys(zip_code)
    # Enter country
    Select(driver.find_element_by_css_selector("#id_country")).select_by_value(country)
    # Enter additional info
    driver.find_element_by_css_selector("#other").send_keys(additional_info)


def enter_phones_email_reference(home_phone, mobile_phone, email_reference):
    # Enter home phone
    driver.find_element_by_css_selector("#phone").send_keys(home_phone)
    # Enter mobile phone
    driver.find_element_by_css_selector("#phone_mobile").send_keys(mobile_phone)
    # Enter email address for future references
    driver.find_element_by_css_selector("#alias").send_keys(email_reference)


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


def sign_up_newsletter_special_offer():
    driver.find_element_by_css_selector("#newsletter").click()
    driver.find_element_by_css_selector("#optin").click()


open_browser(url="http://automationpractice.com/index.php", browser="firefox")
# Enter invalid email address and check error message
enter_email_address("bbb@.g.com")
check_error_text()
# Enter valid email address
enter_email_address("bbb@gg.com")
enter_name_password_gender(firstname="Nicholas", lastname="Johnson", password="Johnson")
enter_date(day="11  ", month="May ", year="2001  ")
sign_up_newsletter_special_offer()
# Enter address information
enter_firstname_lastname_company(first_name="Bernard", last_name="Lampard", company="Foormols")
enter_addresses_city_state(address="1622 E Ayre Street", address2="Sas1120", city="Honk-Kong", state="Arizona")
enter_zip_country_info(zip_code="15444", country="21", additional_info="I am an engineer\nI live in Yerevan")
enter_phones_email_reference(home_phone="+37455997711", mobile_phone="+37455883300", email_reference="Mango@ss.com")

# Register all data
# driver.find_element_by_css_selector(".//*[@id='submitAccount']").click()

close_browser(timeout=3)
