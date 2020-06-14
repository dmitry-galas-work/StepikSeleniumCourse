import os
from selenium import webdriver
import time

print(os.path.abspath(__file__))
print(os.path.abspath(os.path.dirname(__file__)))

try:
    link='http://suninjuly.github.io/file_input.html'
    browser = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element_by_css_selector('input[name="firstname"]')
    input1.send_keys('Name')

    input2 = browser.find_element_by_css_selector('input[name="lastname"]')
    input2.send_keys('Last')

    input3 = browser.find_element_by_css_selector('input[name="email"]')
    input3.send_keys('my@mail.com')

    file_button = browser.find_element_by_css_selector('input[type="file"]')
    file_button.send_keys(r'C:\Users\Admin\Desktop\images\белка-bmp.bmp')

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()