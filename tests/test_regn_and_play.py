import pytest
from faker import Faker

from pages.account_page import AccountPage
from pages.casino_page import CasinoPage
from pages.menu_page import MenuPage
from pages.registration_page import RegistrationPage


@pytest.fixture(scope='function')
def random_user_data():
    fake = Faker()
    user_data = {
        'nickname': fake.user_name(),
        'email': fake.email(),
        'password': fake.password()
    }
    return user_data


def test_registration(page, random_user_data):
    # Регистрация нового пользователя
    registration_page = RegistrationPage(page)
    registration_page.open_registration_page()
    registration_page.fill_registration_form(random_user_data)
    registration_page.submit_registration()

    # Проверка информации об аккаунте
    account_page = AccountPage(page)
    account_page.check_account_information(random_user_data)

    # Проверка баланса игрока
    # Баланс отображается при входе в аккаунт

    # Запуск первой игры в казино
    casino_page = CasinoPage(page)
    casino_page.launch_first_casino_game()

    # Выход из аккаунта
    menu_page = MenuPage(page)
    menu_page.logout()

    # Попытка регистрации с уже существующими данными
    registration_page.registration_with_existing_user(random_user_data)
