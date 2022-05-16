from selenium.webdriver.common.by import By


class MainPageLocators():
    '''
    Класс для хранения селекторов для главной страницы сайта
    '''
    # эта константа будет представлять собой кортеж (метод поиска, что ищем)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")