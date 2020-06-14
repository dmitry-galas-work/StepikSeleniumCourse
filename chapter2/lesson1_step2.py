import math
import time
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/math.html"
    browser = webdriver.Chrome()
    browser.get(link)

    text_x = browser.find_element_by_css_selector('span#input_value')
    result=calc(text_x.text)

    input1= browser.find_element_by_css_selector('input#answer')
    input1.send_keys(result)

    checkbox = browser.find_element_by_css_selector('input#robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_css_selector('[for="robotsRule"]')
    radio.click()

    button_submit = browser.find_element_by_css_selector('button.btn.btn-default[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()