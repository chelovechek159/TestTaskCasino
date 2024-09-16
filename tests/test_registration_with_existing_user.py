from config import URL, browser
from user_data import user_data


def reg_with_exist_user(page):
    page.goto(URL)
    page.click('div.SimpleButton:has-text("Sign up")')  # Нажимаем кнопку регистрации
    # Заполняем форму регистрации
    page.fill('input[type="text"][tabindex="0"].Input.with_clear_button', user_data['nickname'])
    page.fill('input[type="email"]', user_data['email'])
    page.fill('input[type="password"]', user_data['password'])
    page.fill('div.password_confirm-field-container input[type="password"]', user_data['password'])
    # Нажимаем кнопку подтвердить
    page.click('div.panel.SimpleButton.SimpleButton_use_text.send-form')
    page.wait_for_selector('.FormField__error_text')
    assert page.is_visible('.FormField__error_text'), "Владелец зарегистрировался с существующими данными"


def test_registration_with_existing_user(browser):
    page = browser.new_page()  # Создаём новую страницу
    reg_with_exist_user(page)  # Пробуем зарегистрироваться с существующими данными
    page.close()
