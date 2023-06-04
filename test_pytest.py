import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time


def test_registration():
    link = "http://suninjuly.github.io/registration2.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    input1 = browser.find_element(By.TAG_NAME, "input")
    input1.send_keys("Ivan")
    input2 = browser.find_element(By.XPATH, "//input[@placeholder='Input your last name']")
    input2.send_keys("Petrov")
    input3 = browser.find_element(By.CLASS_NAME, "form-control.third")
    input3.send_keys("Smolensk@mail.ru")

    button = browser.find_element(By.CSS_SELECTOR, "button.btn")
    button.click()



    if __name__ == "__main__":
        pytest.main()
