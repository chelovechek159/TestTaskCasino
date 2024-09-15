from infrastructure.config import get_config

class LoginPage:
    LOGIN_BUTTON = 'div.SimpleButton:has-text("Login")'
    USERNAME_INPUT = 'input[name="username"]'
    PASSWORD_INPUT = 'input[name="password"]'
    SIGN_IN_BUTTON = '.LoginContainer__sign_in_action'

    def __init__(self, page):
        self.page = page

    def open(self):
        self.page.goto(get_config().get('url'))
        self.page.wait_for_selector(self.LOGIN_BUTTON)

    def login(self):
        self.page.click(self.LOGIN_BUTTON)
        self.page.wait_for_selector(self.USERNAME_INPUT)
        self.page.fill(self.USERNAME_INPUT, get_config().get("auth_data").get("login"))
        self.page.fill(self.PASSWORD_INPUT, get_config().get("auth_data").get("password"))
        self.page.click(self.SIGN_IN_BUTTON)
        self.page.wait_for_timeout(2000)  # Ожидание после авторизации для корректной загрузки страницы
