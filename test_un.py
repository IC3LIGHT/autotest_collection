from selenium import webdriver
from selenium.webdriver.common.by import By
import time
import unittest


class TestRegistration(unittest.TestCase):
    def test_reg1(self):
        link = "http://suninjuly.github.io/registration1.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CLASS_NAME, 'form-control.first')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CLASS_NAME, 'form-control.second')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CLASS_NAME, 'form-control.third')
        input3.send_keys("Ivan@Ivanov.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")

    def test_reg2(self):
        link = "http://suninjuly.github.io/registration2.html"
        browser = webdriver.Chrome()
        browser.get(link)
        input1 = browser.find_element(By.CSS_SELECTOR,
                                      'div[class="first_block"] > div[class="form-group first_class"] > input['
                                      'class="form-control first"]')
        input1.send_keys("Ivan")
        input2 = browser.find_element(By.CSS_SELECTOR,
                                      'div[class="first_block"] > div[class="form-group second_class"] > input['
                                      'class="form-control second"]')
        input2.send_keys("Ivanov")
        input3 = browser.find_element(By.CSS_SELECTOR, 'div[class="first_block"] > div[class="form-group '
                                                       'third_class"] > input[class="form-control third"]')
        input3.send_keys("Ivan@Ivanov.com")
        button = browser.find_element(By.CSS_SELECTOR, "button.btn")
        button.click()
        time.sleep(1)

        welcome_text_elt = browser.find_element(By.TAG_NAME, "h1")
        welcome_text = welcome_text_elt.text
        self.assertEqual(welcome_text, "Congratulations! You have successfully registered!", "Registration failed")


if __name__ == "__main__":
    unittest.main()
