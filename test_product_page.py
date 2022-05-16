import pytest
from pages.product_page import ProductPage


class TestProduct:
    '''Класс, охватывающий тесты со страницей товаров'''
    @pytest.mark.skip
    def test_guest_can_add_product_to_basket(browser):
        '''
        Тест для проверки возможности добавления товара в корзину
        :param browser: фикстура - драйвер браузера
        :return: None
        '''
        # link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser=browser, url=link)
        page.open()
        # вызываем метод добавления в корзину
        page.add_product_to_basket()
        # вызываем метод ввода проверочного кода для задания stepik
        page.solve_quiz_and_get_code()
        # метод проверки наличия сообщения об успешном добавлении товара
        page.should_be_added_to_basket()

    @pytest.mark.skip
    @pytest.mark.parametrize('i_link', ["http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer0",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer1",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer2",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer3",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer4",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer5",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer6",
                                        # помечаем один из параметров, как приводящий к падению теста
                                        pytest.param(
                                            "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer7",
                                            marks=pytest.mark.xfail),
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer8",
                                        "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer9"])
    def test_guest_can_add_product_to_basket_with_parametrize(browser, i_link):
        '''
        Этот тест копия предыдущего, за исключением того, что он выполняется с разными параметрами
        :param browser:
        :param url: str - ссылка страницы
        :return: None
        '''
        page = ProductPage(browser=browser, url=i_link)
        page.open()
        # вызываем метод добавления в корзину
        page.add_product_to_basket()
        # вызываем метод ввода проверочного кода для задания stepik
        page.solve_quiz_and_get_code()
        # метод проверки наличия сообщения об успешном добавлении товара
        page.should_be_added_to_basket()

    @pytest.mark.xfail
    def test_guest_cant_see_success_message_after_adding_product_to_basket(browser):
        '''
        Тест для проверки отсутствия сообщения об успешном добавлении товара в корзину,
         после нажатия на кнопку добавления товара.
         '''
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.add_product_to_basket()
        page.solve_quiz_and_get_code()
        page.should_not_be_success_message()

    def test_guest_cant_see_success_message(browser):
        '''
        Тест для проверки отсутствия сообщения об успешном добавлении товара,
        без нажатия на кнопку добавления товара в корзину
        '''
        link = 'http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019'
        page = ProductPage(browser=browser, url=link)
        page.open()
        page.should_not_be_success_message()


class TestLogin():
    '''Класс, охватывающий тесты работы со страницей логина'''
    def test_guest_should_see_login_link_on_product_page(browser):
        '''
        Тест для проверки наличия у пользователя - гостя ссылки для перехда на страницу логина.
        :param browser:
        :return: None
        '''
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.should_be_login_link()

    def test_guest_can_go_to_login_page_from_product_page(browser):
        '''
        Тест для проверки возможности перехода гостя на страницу логина
        :param browser:
        :return: None
        '''
        link = "http://selenium1py.pythonanywhere.com/en-gb/catalogue/the-city-and-the-stars_95/"
        page = ProductPage(browser, link)
        page.open()
        page.go_to_login_page()


'''НИЖЕ ПРИМЕР КЛАССА С ФИКСТУРОЙ СОЗДАНИЯ И УДАЛЕНИЯ ДАННЫХ В БД, ЧЕРЕЗ API'''


@pytest.mark.skip
@pytest.mark.login
class TestLoginFromProductPage():
    @pytest.fixture(scope="function", autouse=True)
    def setup(self):
        '''Метод для создания исходных данных для теста и удаления их по окончании.'''
        # строка ниже закоментирована в связи с отсутствием класса ProductFactory и носит демонстрационный характер
        # self.product = ProductFactory(title="Best book created by robot")
        # создаем по апи
        self.link = self.product.link
        yield
        # после этого ключевого слова начинается teardown
        # выполнится после каждого теста в классе
        # удаляем те данные, которые мы создали
        self.product.delete()

    def test_guest_can_go_to_login_page_from_product_page(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста

    def test_guest_should_see_login_link(self, browser):
        page = ProductPage(browser, self.link)
        # дальше обычная реализация теста
