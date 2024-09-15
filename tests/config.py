# config.py
import pytest
from playwright.sync_api import sync_playwright

URL = 'https://poker.evenbetpoker.com/html5'


@pytest.fixture(scope="module")
def browser():  # Фикстура для запуска браузера.
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Открываем браузер
        yield browser  # Возвращаем объект браузера для тестов
        browser.close()  # Закрываем браузер после завершения тестов
