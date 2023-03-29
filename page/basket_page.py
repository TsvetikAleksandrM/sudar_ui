from utils.common import wait

from locators.basket_locators import *
from page.base_page import BasePage, log


class BasketPage(BasePage):
    """Класс для работы со страницей 'Корзина'"""

    name = 'basket_page'

    def ordering_text_is_visible(self):
        """Определяет видимость текста 'Оформление заказа'"""
        return self.element_is_visible(ordering_text)

    @log
    def wait_ordering_text(self):
        """Ожидает отображение текста 'Оформление заказа'"""
        wait(lambda: self.ordering_text_is_visible(), err_msg='Text "Ordering" isn`t visible')

    @log
    def click_delete_product_card_button(self, product):
        """Кликает по кнопке 'Удалить' в карточке продукта"""
        self.click_element(delete_product_card_button.format(product=product))

    @log
    def your_basket_is_empty_text_is_visible(self):
        """Определяет видимость текста 'Ваша корзина пуста'"""
        return self.element_is_visible(your_basket_is_empty_text)
