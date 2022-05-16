from pages.main_page import MainPage
from pages.login_page import LoginPage


def test_guest_can_go_to_login_page(browser):
    '''
    Тест, который открывает страницу и переходит на страницу логина
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = "http://selenium1py.pythonanywhere.com/"
    # инициализируем Page Object, передаем в конструктор экземпляр драйвера и url адрес
    page = MainPage(browser, link)
    # открываем страницу
    page.open()
    # выполняем метод страницы — переходим на страницу логина
    page.go_to_login_page()
    # создаём инстанс класса - страницы логина, передав
    # ему под управление текущий браузер и текущей URL адрес в браузере
    login_page = LoginPage(browser, browser.current_url)
    # вызываем один из методов класса - страницы логина
    login_page.should_be_login_page()


def test_guest_should_see_login_link(browser):
    '''
    Тест, который проверяет наличие ссылки для логина на странице
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()


def test_guest_should_see_login_form(browser):
    '''
    Тест, который проверяет наличие формы для логина
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_form()


def test_guest_should_see_register_form(browser):
    '''
    Тест для определения наличия на страницы формы для регистрации
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_register_form()


def test_guest_should_see_substring_in_url(browser):
    '''
    Тест для проверки наличия подстроки в URL адресе
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = 'http://selenium1py.pythonanywhere.com/ru/accounts/login/'
    page = LoginPage(browser, link)
    page.open()
    page.should_be_login_url(substring='login')