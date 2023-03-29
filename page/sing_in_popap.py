from locators.sing_in_locators import *
from page.base_page import BasePage, log
from utils.common import wait


class SignInPopap(BasePage):
    """Класс для работы с попапом 'Войти'"""

    name = 'sign_in_popap'

    def email_field_is_visible(self):
        """Определяет видимость поля 'Электронная почта'"""
        return self.element_is_visible(email_field)

    @log
    def wait_email_field(self):
        """Ожидает отображение поля 'Электронная почта'"""
        wait(lambda: self.email_field_is_visible(), err_msg='"Email" field isn`t visible')

    @log
    def enter_to_email(self, email):
        """Вводит текст в поле 'Электронная почта'"""
        self.enter_text_in_field(email, email_field)

    @log
    def enter_to_password(self, password):
        """Вводит текст в поле 'Введите пароль'"""
        self.enter_text_in_field(password, password_field)

    @log
    def click_come_button_in_auth_popup(self):
        """Кликает по кнопке 'Войти'"""
        self.click_element(come_button_in_auth_popup)

    @log
    def sign_in(self, email, password):
        """Авторизовывает пользователя с указанными кредами"""
        self.click_come_in_button()
        self.wait_email_field()
        self.enter_to_email(email)
        self.enter_to_password(password)
        self.click_come_button_in_auth_popup()
