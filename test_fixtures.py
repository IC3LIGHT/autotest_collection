from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait
import time
import pytest
import math

@pytest.fixture
def browser():
    browser = webdriver.Chrome()
    yield browser
    time.sleep(5)
    browser.quit()

@pytest.mark.parametrize('numb', ["236895", "236896", "236897", "236898", "236899", "236903", "236904", "236905"])
def test_login(browser, numb):
     browser.get(f'https://stepik.org/lesson/{numb}/step/1')
     browser.implicitly_wait(30)
     browser.find_element(By.ID, 'ember33').click()
     browser.find_element(By.ID, 'id_login_email').send_keys('') #ПОЧТА
     browser.find_element(By.ID, 'id_login_password').send_keys('') #ПАРОЛЬ
     browser.find_element(By.CLASS_NAME, 'sign-form__btn.button_with-loader').click()
     time.sleep(5)
     answer = math.log(int(time.time()))
     browser.find_element(By.TAG_NAME, 'textarea').send_keys(answer)
     WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CLASS_NAME, "submit-submission"))).click()
     rez = browser.find_element(By.CLASS_NAME, 'smart-hints__hint').text
     time.sleep(5)
     assert rez == 'Correct!', 'wrong'