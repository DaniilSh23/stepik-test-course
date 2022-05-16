from .base_page import BasePage
from .locators import ProductPageLocator


class ProductPage(BasePage):
    '''Класс для работы со страницей товаров'''

    def add_product_to_basket(self):
        '''
        Метод для добавления товара в корзину.
        :return: None
        '''
        button = self.browser.find_element(*ProductPageLocator.ADD_PRODUCT_TO_BASKET)
        button.click()

