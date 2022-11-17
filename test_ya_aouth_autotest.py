import pytest
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By

LINK = "..."
LOGIN = '...'
PASSWORD = '^&^SNn09VfvA09Mno89oZ^&^'

@pytest.fixture
def browser():
    chrome_options = Options()
    # chrome_options.add_argument("--headless") # включаем режим работы браузера без открытия окна на мониторе
    browser = webdriver.Chrome(options=chrome_options)
    return browser


class TestYandexAouth():
    def test_guest_should_get_login(self, browser):
        browser.get(LINK)
        browser.find_element(By.CSS_SELECTOR, '[data-t="button:default"]').click()
        sleep(1.0)

        browser.find_element(By.ID, "passp-field-login").send_keys(LOGIN)
        browser.find_element(By.ID, 'passp:sign-in').click()
        sleep(2.5)

        browser.find_element(By.ID, "passp-field-passwd").send_keys(PASSWORD)
        browser.find_element(By.ID, 'passp:sign-in').click()
        sleep(5.0)

        browser.find_element(By.CSS_SELECTOR, '[class="UserID-Avatar "]')