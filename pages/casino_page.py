class CasinoPage:
    CASINO_SECTION = 'text="Casino"'
    FIRST_GAME_SELECTOR = '.WidgetCasinoGameListItemContainer'
    PLAY_BUTTON = '.WidgetCasinoGameListItemContainer__play'
    GAME_WIDGET = '.WidgetCasinoGameListGamesPlayerItemContainer__game_widget_wrapper'
    ERROR_MESSAGE = '.error-message'

    def __init__(self, page):
        self.page = page

    def open_casino(self):
        self.page.wait_for_selector(self.CASINO_SECTION)
        self.page.click(self.CASINO_SECTION)
        self.page.wait_for_selector(self.FIRST_GAME_SELECTOR)

    def select_first_game(self):
        first_game = self.page.query_selector(self.FIRST_GAME_SELECTOR)
        return first_game

    def launch_first_casino_game(self):
        self.page.wait_for_selector(self.CASINO_SECTION)
        self.page.click(self.CASINO_SECTION)
        self.page.wait_for_selector(self.FIRST_GAME_SELECTOR)
        first_game = self.page.query_selector(self.FIRST_GAME_SELECTOR)
        first_game.hover()
        self.page.wait_for_selector(self.PLAY_BUTTON)
        self.page.click(self.PLAY_BUTTON)
        self.page.wait_for_timeout(7000)
        assert self.page.is_visible(self.GAME_WIDGET), "Игровое поле не отображается"
        assert not self.page.is_visible(self.ERROR_MESSAGE), "Обнаружено сообщение об ошибке при запуске игры"