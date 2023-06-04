from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep
import pytest

class TestAbs:
    def test_abs1(self):
        link = "http://suninjuly.github.io/registration1.html"
        chrome = webdriver.Chrome()
        chrome.get(link)
        first_name_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .first')
        last_name_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .second')
        email_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .third')
        button = chrome.find_element(By.XPATH, '//button[@type="submit"]')
        first_name_input_field.send_keys("Bruh")
        last_name_input_field.send_keys("Bruhov")
        email_input_field.send_keys("bruh@bruh.com")
        button.click()
        sleep(2)
        rez = chrome.find_element(By.TAG_NAME, 'h1').text

        assert "Congratulations! You have successfully registered!" == rez
        sleep(3)


    def test_abs2(self):
        link = "http://suninjuly.github.io/registration2.html"
        chrome = webdriver.Chrome()
        chrome.get(link)
        first_name_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .first')
        last_name_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .second')
        email_input_field = chrome.find_element(By.CSS_SELECTOR, '.first_block .third')
        button = chrome.find_element(By.XPATH, '//button[@type="submit"]')
        first_name_input_field.send_keys("Bruh")
        last_name_input_field.send_keys("Bruhov")
        email_input_field.send_keys("bruh@bruh.com")
        button.click()
        sleep(2)
        rez = chrome.find_element(By.TAG_NAME, 'h1').text
        assert "Congratulations! You have successfully registered!" == rez
        sleep(3)


if __name__ == "__main__":
    pytest.main()