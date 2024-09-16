from config import URL, browser
from user_data import user_data


def launch_first_casino_game(page):
    page.goto(URL)  # Переход на сайт
    # Авторизация
    page.wait_for_selector('div.SimpleButton:has-text("Login")')
    page.click('div.SimpleButton:has-text("Login")')
    page.fill('input[name="username"]', user_data['nickname'])
    page.fill('input[name="password"]', user_data['password'])
    page.click('.LoginContainer__sign_in_action')  # Нажимаем кнопку входа (Login)

    # Переход в раздел казино и запуск игры
    page.wait_for_selector('text="Casino"')
    page.click('text="Casino"')

    page.wait_for_selector('.WidgetCasinoGameListItemContainer')  # Ожидание появления игр
    first_game = page.query_selector('.WidgetCasinoGameListItemContainer')  # Находим первую ячейку игры
    first_game.hover()  # Навести мышь на ячейку игры

    page.wait_for_selector('.WidgetCasinoGameListItemContainer__play')  # Ожидание кнопки запуска
    page.click('.WidgetCasinoGameListItemContainer__play')  # Нажимаем на кнопку "Запустить игру"

    page.wait_for_timeout(7000)  # Ждем загрузки игры
    assert page.is_visible('.WidgetCasinoGameListGamesPlayerItemContainer__game_widget_wrapper'), \
        "Игровое поле не отображается"


def test_launch_game(browser):
    page = browser.new_page()  # Создаём новую страницу
    launch_first_casino_game(page)  # Запускаем первую игру в казино
    page.close()
