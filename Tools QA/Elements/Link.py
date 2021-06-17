#!/usr/bin/env python3

import time
from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def close_browser(timeout):
    time.sleep(timeout)
    driver.close()


# def there_is_window_other_than(windows):
#     handles = driver.window_handles
#     for w in windows:
#         handles.remove(w)
#     return handles[-1] if len(handles) > 0 else False


driver = webdriver.Firefox()
driver.get("https://demoqa.com/links")
driver.implicitly_wait(10)

current_window = driver.current_window_handle
old_windows = driver.window_handles
radioNo = driver.find_element_by_css_selector("div#linkWrapper #simpleLink").click()
handles = driver.window_handles
for w in old_windows:
    handles.remove(w)
new_window = handles[-1]
WebDriverWait(driver, 15).until(EC.new_window_is_opened(old_windows))

driver.switch_to.window(new_window)
close_browser(timeout=3)

driver.switch_to.window(current_window)
close_browser(timeout=3)