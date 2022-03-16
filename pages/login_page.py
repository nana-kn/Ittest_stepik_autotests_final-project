from .base_page import BasePage
from .locators import MainPageLocators
from .locators import LoginPageLocators
import time


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, 'Страница по данному url-адресу не найдена'

    def should_be_login_form(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_FORM), 'Форма логина отсутствует'

    def should_be_register_form(self):
        assert self.is_element_present(*MainPageLocators.REGISTRATION_FORM), "Форма регистрации отсутствует"
    
    def register_new_user(self, email, password):
        fild_email = self.browser.find_element(*LoginPageLocators.EMAIL)
        fild_email.send_keys(email)
        fild_password = self.browser.find_element(*LoginPageLocators.PASSWORD)
        fild_password.send_keys(password)
        fild_password_confirm = self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD)
        fild_password_confirm.send_keys(password)
        button = self.browser.find_element(*LoginPageLocators.BUTTON_REGISTER)
        button.click()
        
    