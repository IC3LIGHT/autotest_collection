from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
#from selenium.common.exceptions import TimeoutException  - если появятся тех. работы
import time

email = ''  # почта от зарегистрированного аккаунта яндекс
password = ''  # пароль от зарегистрированного аккаунта яндекс
link = "https://csgofastx.com"
options = Options()
options.add_argument('--disable-notifications')  # отключение начального оповещения
browser: WebDriver = webdriver.Chrome(options=options)
browser.get(link)
main_window = browser.window_handles[0]

try:
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.CSS_SELECTOR, '.controls-panel__buttons > .transparent-btn:nth-child(1)'))).click()
    browser.find_element(By.CLASS_NAME, "btn.btn-primary").click()
    browser.find_element(By.CLASS_NAME, 'btn.social-item-button.yandex.ng-star-inserted').click()
    new_window = browser.window_handles[1]
    browser.switch_to.window(new_window)
    browser.implicitly_wait(5)
    browser.find_element(By.CSS_SELECTOR, '#passp-field-login').send_keys(email)
    browser.find_element(By.ID, 'passp:sign-in').click()
    browser.find_element(By.CSS_SELECTOR, '#passp-field-passwd').send_keys(password)
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'passp:sign-in'))).click()
    browser.implicitly_wait(10)

    """ПОПОЛНЕНИЕ"""
    browser.switch_to.window(main_window)
    WebDriverWait(browser, 10).until(EC.presence_of_element_located((By.XPATH, '//a[contains(@href, "/refill")]'))).click()
    """ЕСЛИ ПОЯВИТСЯ ОПОВЕЩЕНИЕ О ТЕХ.РАБОТАХ"""

    #WebDriverWait(browser, 30).until(EC.element_to_be_clickable((By.CLASS_NAME, 'close_modal.close-icons'))).click()
#except TimeoutException:
    #pass

    """ВЫБОР СТРАНЫ"""
    frame = browser.find_element(By.CSS_SELECTOR, "#bb_frame")
    browser.switch_to.frame(frame)
    browser.find_element(By.CSS_SELECTOR, '.dropdown-toggle--country-popup').click()
    browser.find_element(By.XPATH, "/html/body/div[6]/div/ul/li[186]").click()
    WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.CSS_SELECTOR, '.country-popup__close-btn'))).click()
    browser.implicitly_wait(6)

    """ВЫБОР ПЛАТЕЖНОГО ПРОВАЙДЕРА"""
    btc = browser.find_element(By.XPATH, "/html/body/div[3]/div[1]/main/div/div[2]/div/div/div[4]/div[2]/a[5]")
    actions = ActionChains(browser)
    actions.move_to_element(btc).perform()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.XPATH, '/html/body/div[3]/div[1]/main/div/div[2]/div/div/div[4]/div[2]/a[5]'))).click()
    WebDriverWait(browser, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, '.btn.btn-primary.refill-common-button'))).click()

finally:
    time.sleep(10)
    browser.quit()
