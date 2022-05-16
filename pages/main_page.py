from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    '''Главная страница и методы работы с ней'''

    def __init__(self, *args, **kwargs):
        '''Все методы, в классе BasePage.
        Вызываем его конструктор и передаём туда все аргументы, переданные в конструктор MainPage'''
        super(MainPage, self).__init__(*args, **kwargs)