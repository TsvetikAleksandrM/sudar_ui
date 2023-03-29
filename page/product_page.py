from locators.product_locators import *
from page.base_page import BasePage, log


class ProductPage(BasePage):
    """Класс для работы со страницей 'Продукт'"""

    name = 'product_page'

    @log
    def click_add_in_basket_button(self):
        """Кликает по кнопке 'Добавить в корзину'"""
        self.click_element(add_in_basket_button)

    @log
    def added_in_basket_button_is_visible(self):
        """Определяет видимость кнопки 'Добавлено'"""
        return self.element_is_visible(added_in_basket_button)
