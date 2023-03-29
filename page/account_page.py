from locators.account_locators import *
from page.base_page import BasePage, log


class AccountPage(BasePage):
    """Класс для работы со страницей 'Аккаунт'"""

    name = 'account_page'

    @log
    def data_updated_message_is_visible(self):
        """Определяет, видно ли всплывающее сообщение 'Данные обновлены'"""
        return self.element_is_visible(data_updated_message)

    @log
    def enter_to_phone(self, phone):
        """Вводит текст в поле 'Телефон'"""
        self.enter_text_in_field(phone, phone_field)

    @log
    def scroll_to_save_button(self):
        """Скроллит до кнопки 'Сохранить'"""
        self.scroll_to_locator(save_button, y_offset=-200)

    @log
    def click_save_button(self):
        """Кликает по кнопке 'Сохранить'"""
        self.click_element(save_button)
