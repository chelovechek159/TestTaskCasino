from config import URL, browser
from user_data import auth_user_data


def login(page):  # Функция для авторизации на сайте.
    page.goto(URL)  # Зайти на сайт онлайн-казино

    # Ждём появления кнопки "Login" и нажимаем её
    page.wait_for_selector('div.SimpleButton:has-text("Login")')
    page.click('div.SimpleButton:has-text("Login")')

    # Ждём появления полей ввода и вводим данные для авторизации
    page.wait_for_selector('input[name="username"]')
    page.fill('input[name="username"]', auth_user_data['username'])
    page.fill('input[name="password"]', auth_user_data['password'])
    page.click('.LoginContainer__sign_in_action')  # Нажимаем кнопку входа (Login)


def navigate_to_casino(page):  # Функция для навигации в раздел казино.
    # Проверяем, что мы находимся в казино
    page.wait_for_selector('text="Casino"')
    page.click('text="Casino"')  # Выбираем раздел казино


def select_first_game(page):  # Функция для выбора первой игры в казино.
    # Ждём появления игр и выбираем первую
    page.wait_for_selector('.WidgetCasinoGameListItemContainer')
    first_game = page.query_selector('.WidgetCasinoGameListItemContainer')

    assert first_game is not None, "First game item not found!"  # Проверка, что игра найдена

    first_game.hover()  # Навести мышь на ячейку игры
    page.wait_for_selector('.WidgetCasinoGameListItemContainer__play')
    page.click('.WidgetCasinoGameListItemContainer__play')  # Клик по кнопке "Запустить игру"


def verify_game_loaded(page):  # Функция для проверки загрузки игры.
    # Подождать несколько секунд, чтобы убедиться, что игра запущена и загружена
    page.wait_for_timeout(6500)

    # Проверяем, что игра запустилась
    assert page.is_visible('.WidgetCasinoGameListGamesPlayerItemContainer__game_widget_wrapper'), \
        "Игровое поле не отображается"


def test_auth_and_play(browser):  # Тест для авторизации и запуска игры в онлайн-казино.
    page = browser.new_page()  # Открыть новую страницу
    login(page)  # Выполняем авторизацию
    navigate_to_casino(page)  # Переходим в раздел казино
    select_first_game(page)  # Выбираем первую игру
    verify_game_loaded(page)  # Проверяем, что игра загрузилась

    # Закрыть страницу
    page.close()
