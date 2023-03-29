from random import choice
from utils.common import wait

from locators.catalog_locators import *
from page.base_page import BasePage, log


class CatalogPage(BasePage):
    """Класс для работы со страницей 'Каталог'"""

    name = 'catalog_page'

    def you_searched_text_is_visible(self):
        """Определяет видимость текста 'Вы искали <<...>>'"""
        return self.element_is_visible(you_searched_text)

    @log
    def wait_you_searched_text(self):
        """Ожидает отображение текста 'Вы искали <<...>>'"""
        wait(lambda: self.you_searched_text_is_visible(), err_msg='"You searched" text isn`t visible')

    @log
    def open_random_card(self):
        """Открывает рандомную карточку с продуктом"""
        cards = self.get_elements(product_cards)
        random_cards = choice(cards)
        self.move_mouse_to_element(random_cards)
        random_cards.click()
