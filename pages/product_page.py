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

    def should_be_added_to_basket(self):
        '''
        Метод для проверки наличия сообщения об успешном добавлении товара в корзину
        :return: None
        '''
        assert self.is_element_present(*ProductPageLocator.CHECKING_ADD_TO_BASKET), '===No add to basket message==='

    def should_not_be_success_message(self):
        '''
        Метод для проверки отсутствия элемента на странице в течение заданного времени (по умолчанию 4 сек.)
        :return: None
        '''
        assert self.is_not_element_present(*ProductPageLocator.CHECKING_ADD_TO_BASKET), \
            "Success message is presented, but should not be"




