import pytest
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


class ProductPageLocator():
    '''
    Класс для хранения локаторов для страницы с товарами
    '''
    ADD_PRODUCT_TO_BASKET = (By.CSS_SELECTOR, '.btn.btn-lg.btn-primary.btn-add-to-basket')
    CHECKING_ADD_TO_BASKET = (By.CSS_SELECTOR, '#messages')
    SUCCESS_MESSAGE = (By.CSS_SELECTOR, 'some-class-for-success')   # это несуществующий локатор для примера


class BasePageLocators():
    '''
    Базовый класс для хранения локаторов, общих для всех страниц
    '''
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
    LOGIN_LINK_INVALID = (By.CSS_SELECTOR, "#login_link_inc")


