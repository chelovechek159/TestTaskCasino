from pages.casino_page import CasinoPage
from pages.game_page import GamePage
from pages.login_page import LoginPage


def test_auth_and_play(page):

    # Авторизация
    login_page = LoginPage(page)
    # Переход на сайт
    login_page.open()
    # Авторизация
    login_page.login()
    # Переход в раздел Casino
    casino_page = CasinoPage(page)
    # Переход в Casino
    casino_page.open_casino()
    # Выбор и запуск игры
    game_page = GamePage(page)
    # Выбор первой игры и запуск
    first_game = casino_page.select_first_game()
    game_page.start_first_game(first_game)
