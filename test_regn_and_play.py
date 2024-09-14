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
        print('Открываем браузер')
        yield browser  # Возвращаем объект браузера для тестов
        browser.close()  # Закрываем браузер после завершения тестов


def test_regn(browser):
    page = browser.new_page()  # Создаём новую страницу
    page.goto(url)

    # Ждём появления кнопки регистрация
    page.wait_for_selector('div.SimpleButton:has-text("Sign up")')
    page.click('div.SimpleButton:has-text("Sign up")')  # Нажимаем кнопку регистрации

    # имя пользователя
    page.fill('input[type="text"][tabindex="0"].Input.with_clear_button', user_data['nickname'])
    # email
    page.fill('input[type="email"]', user_data['email'])
    # пароль
    page.fill('input[type="password"]', user_data['password'])
    # подтверждение пароля
    page.fill('div.password_confirm-field-container input[type="password"]', user_data['password'])

    # Нажимаем кнопку регистрации
    page.click('div.panel.SimpleButton.SimpleButton_use_text.send-form')

    # Нажимаем на кнопку для открытия sideBar menu
    page.click('.menu_button.SimpleButton')
    # Нажимаем на дропдаун Account
    page.click('.LobbySidebarContainer__action.account.SimpleButton:not(.isShowSubAction)')
    # Нажать на кнопку Информация об аккаунте
    page.click('div.LobbySidebarContainer__action.account_info')

    # Получаем отображаемые данные
    displayed_nickname = page.inner_text('div.AccountInformationContainer__form_field.name span')
    displayed_email = page.inner_text('div.AccountInformationContainer__form_field.email span')

    # Проверяем, что отображаемые данные соответствуют отправленным данным
    assert displayed_nickname == user_data['nickname'], f"Ожидалось {user_data['nickname']}, но отображается {displayed_nickname}"
    assert displayed_email == user_data['email'], f"Ожидалось {user_data['email']}, но отображается {displayed_email}"

    page.click('.Dialog__action.cancel')

    page.wait_for_selector('text="Casino"')
    page.click('text="Casino"')

    page.wait_for_selector('.WidgetCasinoGameListItemContainer')  # Ожидание появления игр
    first_game = page.query_selector('.WidgetCasinoGameListItemContainer')  # Находим первую ячейку игры

    # Навести мышь на ячейку игры и запустить игру
    first_game.hover()

    # Ожидание кнопки "Запустить игру"
    page.wait_for_selector('.WidgetCasinoGameListItemContainer__play')  # Ожидание кнопки запуска

    # Клик по кнопке "Запустить игру"
    page.click('.WidgetCasinoGameListItemContainer__play')  # Нажимаем на кнопку "Запустить игру"

    page.wait_for_timeout(10000)
    # Проверяем, что игровое поле загружено
    assert page.is_visible('.WidgetCasinoGameListGamesPlayerItemContainer__game_widget_wrapper'), "Игровое поле не отображается"
    # Проверяем, что на странице нет сообщений об ошибке
    assert not page.is_visible('.error-message'), "Обнаружено сообщение об ошибке при запуске игры"
    # Проверяем, что баланс игрока отображается
    assert page.is_visible('.LobbyHeaderContainer__expand_button'), "Баланс игрока не отображается"

    page.close()
