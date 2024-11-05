class GamePage:
    PLAY_BUTTON = '.WidgetCasinoGameListItemContainer__play'

    def __init__(self, page):
        self.page = page

    def start_first_game(self, game_element):
        game_element.hover()
        self.page.wait_for_selector(self.PLAY_BUTTON)
        self.page.click(self.PLAY_BUTTON)
        self.page.wait_for_timeout(10000)  # Ждём 10 секунд для загрузки игры
