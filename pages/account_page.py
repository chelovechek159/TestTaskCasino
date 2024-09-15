class AccountPage:
    MENU_BUTTON = '.menu_button.SimpleButton'
    ACCOUNT_BUTTON = '.LobbySidebarContainer__action.account.SimpleButton:not(.isShowSubAction)'
    ACCOUNT_INFO_BUTTON = 'div.LobbySidebarContainer__action.account_info'
    NICKNAME_DISPLAY = 'div.AccountInformationContainer__form_field.name span'
    EMAIL_DISPLAY = 'div.AccountInformationContainer__form_field.email span'
    CANCEL_BUTTON = '.Dialog__action.cancel'

    def __init__(self, page):
        self.page = page

    def check_account_information(self, user_data):
        self.page.click(self.MENU_BUTTON)
        self.page.click(self.ACCOUNT_BUTTON)
        self.page.click(self.ACCOUNT_INFO_BUTTON)
        displayed_nickname = self.page.inner_text(self.NICKNAME_DISPLAY)
        displayed_email = self.page.inner_text(self.EMAIL_DISPLAY)
        assert displayed_nickname == user_data['nickname'], f"Ожидалось {user_data['nickname']}, но отображается {displayed_nickname}"
        assert displayed_email == user_data['email'], f"Ожидалось {user_data['email']}, но отображается {displayed_email}"
        self.page.click(self.CANCEL_BUTTON)
