from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
import time
import math

try:
    link = "http://suninjuly.github.io/redirect_accept.html"
    browser: WebDriver = webdriver.Chrome()
    browser.get(link)

    browser.find_element(By.TAG_NAME, "button").click()
    nw = browser.window_handles[1]
    browser.switch_to.window(nw)
    x = browser.find_element(By.ID, 'input_value')
    rez = str(math.log(abs(12 * math.sin(int(x.text)))))
    browser.find_element(By.ID, "answer").send_keys(rez)
    browser.find_element(By.TAG_NAME, "button").click()

    time.sleep(1)


finally:
    time.sleep(10)
    browser.quit()
