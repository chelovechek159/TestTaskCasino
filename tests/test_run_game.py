from pages.casino_page import CasinoPage
from pages.game_page import GamePage
from pages.menu_page import MenuPage
from pages.registration_page import RegistrationPage


def test_launch_game(page, random_user_data):
    # Регистрация нового пользователя
    registration_page = RegistrationPage(page)
    registration_page.open_registration_page()
    registration_page.fill_registration_form(random_user_data)
    registration_page.submit_registration()

    # Запуск первой игры в казино
    casino_page = CasinoPage(page)
    # Переход в Casino
    casino_page.open_casino()
    # Выбор и запуск игры
    game_page = GamePage(page)
    # Выбор первой игры и запуск
    first_game = casino_page.select_first_game()
    game_page.start_first_game(first_game)

    # Выход из аккаунта
    menu_page = MenuPage(page)
    menu_page.logout()
