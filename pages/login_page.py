from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    '''Страница логина и методы проверок её функционала'''

    def should_be_login_page(self):
        '''
        Проверяем страницу логина на предмет наличия подстроки в URL адресе,
        формы для логина пользователя,
        формы для регистрации пользователя,
        путём вызова необходимых методов класса для этого
        :return: None
        '''
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, substring='login'):
        '''
        Метод для проверки наличия подстроки в URL адресе страницы логина
        :param substring: str - искомая подстрока
        :return: None
        '''
        assert substring in self.browser.current_url, f'===Substring = {substring} not found in URL==='

    def should_be_login_form(self):
        '''
        Метод для проверки наличия формы логина на странице
        :return: None
        '''
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), '===Missing LOGIN form==='

    def should_be_register_form(self):
        '''
        Метод для проверки наличия формы регистрации на странице
        :return: None
        '''
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), '===Missing REGISTER form==='