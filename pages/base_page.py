class BasePage():
    def __init__(self, browser, url):
        '''
        Конструктор базового, абстрактного класса
        :param browser: объект браузера
        :param url: str - адрес страницы
        '''
        self.browser = browser
        self.url = url

    def open(self):
        '''
        Метод, который открывает нужную страницу в браузере
        :return: None
        '''
        self.browser.get(self.url)