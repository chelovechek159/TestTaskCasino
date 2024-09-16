from infrastructure.config import get_config


class RegistrationPage:
    SIGN_UP_BUTTON = 'div.SimpleButton:has-text("Sign up")'
    NICKNAME_INPUT = 'input[type="text"][tabindex="0"].Input.with_clear_button'
    EMAIL_INPUT = 'input[type="email"]'
    PASSWORD_INPUT = 'input[type="password"]'
    PASSWORD_CONFIRM_INPUT = 'div.password_confirm-field-container input[type="password"]'
    SUBMIT_BUTTON = 'div.panel.SimpleButton.SimpleButton_use_text.send-form'
    ERROR_MESSAGE = '.FormField__error_text'

    def __init__(self, page):
        self.page = page

    def open_registration_page(self):
        self.page.goto(get_config().get('url'))
        self.page.wait_for_selector(self.SIGN_UP_BUTTON)
        self.page.click(self.SIGN_UP_BUTTON)

    def fill_registration_form(self, user_data):
        self.page.fill(self.NICKNAME_INPUT, user_data['nickname'])
        self.page.fill(self.EMAIL_INPUT, user_data['email'])
        self.page.fill(self.PASSWORD_INPUT, user_data['password'])
        self.page.fill(self.PASSWORD_CONFIRM_INPUT, user_data['password'])


    def submit_registration(self):
        self.page.click(self.SUBMIT_BUTTON)
        self.page.wait_for_timeout(2000)  # Ожидание после авторизации для корректной загрузки страницы

    def registration_with_existing_user(self, user_data):
        self.open_registration_page()
        self.fill_registration_form(user_data)
        self.submit_registration()
        self.page.wait_for_selector(self.ERROR_MESSAGE)
        assert self.page.is_visible(
            self.ERROR_MESSAGE), "Ожидалось сообщение об ошибке при регистрации с существующими данными"
