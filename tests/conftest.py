import pytest
from playwright.sync_api import sync_playwright

@pytest.fixture(scope="session")
def browser():
    # Инициализируем Playwright
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch(headless=False)  # Вы можете изменить браузер и задать headless=True
        yield browser  # Возвращаем браузер для использования в тестах
        browser.close()  # Закрываем браузер после всех тестов

@pytest.fixture(scope="function")
def page(browser):
    # Создаём новую страницу для каждого теста
    context = browser.new_context()
    page = context.new_page()
    yield page
    page.close()
    context.close()
