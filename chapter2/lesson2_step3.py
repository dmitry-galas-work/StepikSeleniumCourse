import math
import time
from selenium import webdriver
from selenium.webdriver.support.ui import Select


def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link = "http://suninjuly.github.io/selects1.html"
    browser = webdriver.Chrome()
    browser.get(link)

    num1 = browser.find_element_by_css_selector('h2 span#num1')
    num2 = browser.find_element_by_css_selector('h2 span#num2')
    result=str(int(num1.text)+int(num2.text))
    print(result)

    select_result = Select(browser.find_element_by_css_selector('select#dropdown'))
    select_result.select_by_visible_text(result)

    button_submit = browser.find_element_by_css_selector('button.btn.btn-default[type="submit"]')
    button_submit.click()

finally:
    time.sleep(10)
    browser.quit()