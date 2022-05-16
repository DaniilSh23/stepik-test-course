from selenium.webdriver.common.by import By


class MainPageLocators():
    '''
    Класс для хранения селекторов для главной страницы сайта
    '''
    # эта константа будет представлять собой кортеж (метод поиска, что ищем)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    '''
    Класс для хранения локаторов для страницы логина
    '''
    LOGIN_FORM = (By.CSS_SELECTOR, '#login_form')
    REGISTER_FORM = (By.CSS_SELECTOR, '#register_form')