from playwright.sync_api import sync_playwright


def auth_and_play():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)  # Открыть браузер
        page = browser.new_page()  # Открыть новую страницу
        url = "https://poker.evenbetpoker.com/html5"
        auth_data = {
            'login': 'john',
            'password': 'poker'
        }

        # Зайти на сайт онлайн-казино
        page.goto(url)

        # Ждём появления кнопки "Login"
        page.wait_for_selector('div.SimpleButton:has-text("Login")')
        # Нажимаем кнопку логина
        page.click('div.SimpleButton:has-text("Login")')

        # Ждём появления модального окна авторизации
        page.wait_for_selector('input[name="username"]')

        # Вводим имя пользователя
        page.fill('input[name="username"]', auth_data['login'])

        # Вводим пароль
        page.fill('input[name="password"]', auth_data["password"])

        # Нажать кнопку входа (Login)
        page.click('.LoginContainer__sign_in_action')

        # Выбрать раздел casino
        page.wait_for_selector('text="Casino"')
        page.click('text="Casino"')

        # Выбрать первую игру
        page.wait_for_selector('.WidgetCasinoGameListItemContainer')  # Ожидание появления игр
        first_game = page.query_selector('.WidgetCasinoGameListItemContainer')  # Находим первую ячейку игры

        # Навести мышь на ячейку игры и запустить игру
        first_game.hover()

        # Ожидание кнопки "Запустить игру"
        page.wait_for_selector('.WidgetCasinoGameListItemContainer__play')

        # Клик по кнопке "Запустить игру"
        page.click('.WidgetCasinoGameListItemContainer__play')

        # Подождать несколько секунд, чтобы убедиться, что игра запущена и загружена
        page.wait_for_timeout(15000)

        # Закрыть браузер
        browser.close()


# Запуск файла
auth_and_play()
