from pages.account_page import AccountPage
from pages.registration_page import RegistrationPage
from pages.menu_page import MenuPage

def test_registration(page, random_user_data):
    # Регистрация нового пользователя
    registration_page = RegistrationPage(page)
    registration_page.open_registration_page()
    registration_page.fill_registration_form(random_user_data)
    registration_page.submit_registration()

    # Проверка информации об аккаунте
    account_page = AccountPage(page)
    account_page.check_account_information(random_user_data)

    # Выход из аккаунта
    menu_page = MenuPage(page)
    menu_page.logout()
