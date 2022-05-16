from selenium.webdriver.common.by import By
from .base_page import BasePage
from .locators import MainPageLocators


class MainPage(BasePage):
    '''Главная страница и методы работы с ней'''

    def go_to_login_page(self):
        '''
        Метод перехода на страницу логина пользователя
        :return: None
        '''
        # так как LOGIN_LINK - это кортеж, мы его раскрываем через *
        # это один из способов перехода на страницу, второй показан в stepik, lesson 4.2, step 9
        link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        '''
        Метод проверки наличия ссылки для логина на странице
        :return: None
        '''
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"