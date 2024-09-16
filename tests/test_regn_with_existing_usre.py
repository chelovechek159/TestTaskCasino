from pages.menu_page import MenuPage
from pages.registration_page import RegistrationPage


def test_registration_with_existing_data(page, random_user_data):
    # Попытка регистрации с уже существующими данными
    registration_page = RegistrationPage(page)
    registration_page.open_registration_page()
    registration_page.fill_registration_form(random_user_data)
    registration_page.submit_registration()

    # Выход из аккаунта
    menu_page = MenuPage(page)
    menu_page.logout()

    # Проверка, что регистрация с существующими данными вызывает ошибку
    registration_page.registration_with_existing_user(random_user_data)
