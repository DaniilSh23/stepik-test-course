from selenium.common.exceptions import NoSuchElementException

class BasePage():
    def __init__(self, browser, url, timeout=10):
        '''
        Конструктор базового, абстрактного класса
        :param browser: объект браузера
        :param url: str - адрес страницы
        '''
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    def open(self):
        '''
        Метод, который открывает нужную страницу в браузере
        :return: None
        '''
        self.browser.get(self.url)

    def is_element_present(self, how, what):
        '''
        Метод проверки наличия элемента
        :param how:  как искать (css, id, xpath и тд)
        :param what: что искать (передаётся строка-селектор)
        :return: bool
        '''
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True