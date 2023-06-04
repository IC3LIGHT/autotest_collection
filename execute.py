import time
import math
from selenium import webdriver
from selenium.webdriver.common.by import By

try:
    browser = webdriver.Chrome()
    browser.get("http://suninjuly.github.io/execute_script.html")

    def calc(x):
        return str(math.log(abs(12 * math.sin(int(x)))))
    x_value = browser.find_element(By.CSS_SELECTOR, "[id='input_value']").text
    result_value = calc(x_value)

    browser.find_element(By.XPATH, "//input[@id='answer']").send_keys(result_value)
    browser.find_element(By.CSS_SELECTOR, "#robotCheckbox").click()
    rb = browser.find_element(By.XPATH, "//input[@id='robotsRule']")
    browser.execute_script("return arguments[0].scrollIntoView(true);", rb)
    rb.click()
    browser.find_element(By.CSS_SELECTOR, "button[type='submit']").click()


finally:
    time.sleep(1)
    browser.quit()
    