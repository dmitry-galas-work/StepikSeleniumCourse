from selenium import webdriver
import math
import time
def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    browser = webdriver.Chrome()
    link = "http://suninjuly.github.io/execute_script.html"
    browser.get(link)

    value = browser.find_element_by_css_selector('label span#input_value')
    result=calc(value.text)

    input = browser.find_element_by_css_selector('input#answer')
    input.send_keys(result)

    checkbox = browser.find_element_by_css_selector('input#robotCheckbox')
    checkbox.click()

    radio = browser.find_element_by_css_selector('input#robotsRule')
    browser.execute_script("return arguments[0].scrollIntoView(true);", radio)
    radio.click()

    button_submit = browser.find_element_by_css_selector('button[type="submit"]')
    browser.execute_script("return arguments[0].scrollIntoView(true);", button_submit)
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()