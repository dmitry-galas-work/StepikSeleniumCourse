import math
from selenium import webdriver
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/alert_accept.html'
    browser = webdriver.Chrome()
    browser.get(link)

    button_blue = browser.find_element_by_css_selector('button[type="submit"]')
    button_blue.click()

    alert = browser.switch_to.alert
    alert.accept()

    value = browser.find_element_by_css_selector('span#input_value')
    result=calc(value.text)
    print(result)

    input_field = browser.find_element_by_css_selector('input#answer')
    input_field.send_keys(result)

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()