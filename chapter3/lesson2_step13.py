import unittest
from selenium import webdriver
import time

class test_register_page(unittest.TestCase):
    def test_link1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.send_keys("Dmitry")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Dmitry2")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("dmitry@myemail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "1st link registration isn't passed")

    def test_link2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)

        # Ваш код, который заполняет обязательные поля
        input1 = browser.find_element_by_css_selector('[placeholder="Input your first name"]')
        input1.send_keys("Dmitry")
        input2 = browser.find_element_by_css_selector('[placeholder="Input your last name"]')
        input2.send_keys("Dmitry2")
        input3 = browser.find_element_by_css_selector('[placeholder="Input your email"]')
        input3.send_keys("dmitry@myemail.com")

        # Отправляем заполненную форму
        button = browser.find_element_by_css_selector("button.btn")
        button.click()

        # Проверяем, что смогли зарегистрироваться
        # ждем загрузки страницы
        time.sleep(1)

        # находим элемент, содержащий текст
        welcome_text_elt = browser.find_element_by_tag_name("h1")
        # записываем в переменную welcome_text текст из элемента welcome_text_elt
        welcome_text = welcome_text_elt.text

        # с помощью assert проверяем, что ожидаемый текст совпадает с текстом на странице сайта
        assert "Congratulations! You have successfully registered!" == welcome_text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "2nd registration isn't passed")


if __name__ == "__main__":
    unittest.main()
