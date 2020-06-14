import math
import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver

def calc(x):
  return str(math.log(abs(12*math.sin(int(x)))))

try:
    link='http://suninjuly.github.io/explicit_wait2.html'
    browser = webdriver.Chrome()
    browser.get(link)

    # говорим Selenium проверять в течение 12 секунд, пока кнопка не станет кликабельной
    button = browser.find_element_by_css_selector('button#book')
    WebDriverWait(browser, 12).until(
        #EC.text_to_be_present_in_element((By.ID, "price"), "$100")
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, "h5#price"), "$100")
    )
    button.click()

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