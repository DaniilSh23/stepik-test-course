from pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    '''
    Тест для проверки возможности добавления товара в корзину
    :param browser: фикстура - драйвер браузера
    :return: None
    '''
    link = 'http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear'
    page = ProductPage(browser=browser, url=link)
    page.open()
    # вызываем метод добавления в корзину
    page.add_product_to_basket()
    # вызываем метод ввода проверочного кода для задания stepik
    page.solve_quiz_and_get_code()