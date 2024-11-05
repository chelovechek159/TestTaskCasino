class MenuPage:
    MENU_BUTTON = '.menu_button.SimpleButton'
    LOGOUT_BUTTON = '.logout.SimpleButton'
    LOGIN_BUTTON = 'div.SimpleButton:has-text("Login")'

    def __init__(self, page):
        self.page = page

    def logout(self):
        self.page.click(self.MENU_BUTTON)
        self.page.click(self.LOGOUT_BUTTON)
        self.page.wait_for_selector(self.LOGIN_BUTTON)
        assert self.page.is_visible(self.LOGIN_BUTTON), "Кнопка входа после выхода не отображается"
