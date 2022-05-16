import math
from selenium.common.exceptions import NoSuchElementException, TimeoutException
from selenium.common.exceptions import NoAlertPresentException # в начале файла
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from pages.locators import BasePageLocators


class BasePage():
    '''Абстрактный класс для наследования страниц сайта'''

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

    def solve_quiz_and_get_code(self):
        '''
        Метод, необходимый дря расчёта значения, чтобы сдать ответ на степике.
        :return: None
        '''
        alert = self.browser.switch_to.alert
        x = alert.text.split(" ")[2]
        answer = str(math.log(abs((12 * math.sin(float(x))))))
        alert.send_keys(answer)
        alert.accept()
        try:
            alert = self.browser.switch_to.alert
            alert_text = alert.text
            print(f"Your code: {alert_text}")
            alert.accept()
        except NoAlertPresentException:
            print("No second alert presented")

    def is_not_element_present(self, how, what, timeout=4):
        '''
        Метод для проверки того, что элемент не появится на странице спустя заданное время.
        Использует явное ожидание.
        :param how: CSS_SELECTOR, ID, XPATH и т.д.
        :param what: сам объект поиска
        :param timeout: int - время ожидания на странице
        :return: bool
        '''
        try:
            WebDriverWait(self.browser, timeout).until(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return True

        return False

    def is_disappeared(self, how, what, timeout=4):
        '''
        Метод, который будет ждать, пока элемент не исчезнет со страницы или 4 секунды.
        Обратный методу is_not_element_present, из-за оборота until_not.
        Использует явное ожидание.
        :param how: CSS_SELECTOR, ID, XPATH и т.д.
        :param what: сам объект поиска
        :param timeout: int - время ожидания на странице
        :return: bool
        '''
        try:
            WebDriverWait(self.browser, timeout, 1, TimeoutException). \
                until_not(EC.presence_of_element_located((how, what)))
        except TimeoutException:
            return False

        return True

    def go_to_login_page(self):
        '''
        Переход на страницу логина пользователя
        :return: None
        '''
        link = self.browser.find_element(*BasePageLocators.LOGIN_LINK)
        link.click()

    def should_be_login_link(self):
        '''
        Проверка наличия ссылки для перехода на страницу логина
        :return: None
        '''
        assert self.is_element_present(*BasePageLocators.LOGIN_LINK), "Login link is not presented"