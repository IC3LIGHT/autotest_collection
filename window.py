from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/alert_accept.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    confirm = browser.switch_to.alert
    confirm.accept()
    time.sleep(1)
    x = browser.find_element(By.ID, 'input_value')
    rez = str(math.log(abs(12 * math.sin(int(x.text)))))
    browser.find_element(By.ID, "answer").send_keys(rez)

    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
