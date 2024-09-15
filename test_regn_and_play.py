import pytest
from playwright.sync_api import sync_playwright
from faker import Faker

fake = Faker()
url = 'https://poker.evenbetpoker.com/html5'
# Генерация фековых валидных данных
user_data = {
    'nickname': fake.user_name(),
    'email': fake.email(),
    'password': fake.password()
}


@pytest.fixture(scope="module")
def browser():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Открываем браузер
        yield browser  # Возвращаем объект браузера для тестов
        browser.close()  # Закрываем браузер после завершения тестов


def open__and_fill_registration_page(page):
    page.goto(url)
    page.wait_for_selector('div.SimpleButton:has-text("Sign up")')
    page.click('div.SimpleButton:has-text("Sign up")')  # Нажимаем кнопку регистрации
    # Заполняем форму регистрации
    page.fill('input[type="text"][tabindex="0"].Input.with_clear_button', user_data['nickname'])
    page.fill('input[type="email"]', user_data['email'])
    page.fill('input[type="password"]', user_data['password'])
    page.fill('div.password_confirm-field-container input[type="password"]', user_data['password'])
    # Нажимаем кнопку регистрации
    page.click('div.panel.SimpleButton.SimpleButton_use_text.send-form')


def check_account_information(page):
    # Открываем меню и проверяем информацию об аккаунте
    page.click('.menu_button.SimpleButton')
    page.click('.LobbySidebarContainer__action.account.SimpleButton:not(.isShowSubAction)')
    page.click('div.LobbySidebarContainer__action.account_info')

    displayed_nickname = page.inner_text('div.AccountInformationContainer__form_field.name span')
    displayed_email = page.inner_text('div.AccountInformationContainer__form_field.email span')

    assert displayed_nickname == user_data['nickname'], \
        f"Ожидалось {user_data['nickname']}, но отображается {displayed_nickname}"
    assert displayed_email == user_data['email'], f"Ожидалось {user_data['email']}, но отображается {displayed_email}"

    page.click('.Dialog__action.cancel')


def check_player_balance(page):
    # Проверяем, что баланс игрока отображается
    assert page.is_visible('.LobbyHeaderContainer__expand_button'), "Баланс игрока не отображается"


def launch_first_casino_game(page):
    # Переход в раздел казино и запуск игры
    page.wait_for_selector('text="Casino"')
    page.click('text="Casino"')

    page.wait_for_selector('.WidgetCasinoGameListItemContainer')  # Ожидание появления игр
    first_game = page.query_selector('.WidgetCasinoGameListItemContainer')  # Находим первую ячейку игры
    first_game.hover()  # Навести мышь на ячейку игры

    page.wait_for_selector('.WidgetCasinoGameListItemContainer__play')  # Ожидание кнопки запуска
    page.click('.WidgetCasinoGameListItemContainer__play')  # Нажимаем на кнопку "Запустить игру"

    page.wait_for_timeout(10000)
    # Проверяем, что игровое поле загружено
    assert page.is_visible('.WidgetCasinoGameListGamesPlayerItemContainer__game_widget_wrapper'), \
        "Игровое поле не отображается"
    assert not page.is_visible('.error-message'), "Обнаружено сообщение об ошибке при запуске игры"


def test_registration(browser):
    page = browser.new_page()  # Создаём новую страницу
    open__and_fill_registration_page(page)  # Открываем и заполняем страницу регистрации
    check_account_information(page)  # Проверяем данные аккаунта
    check_player_balance(page)  # Проверяем баланс
    launch_first_casino_game(page)  # Запускаем игру в казино
    page.close()
