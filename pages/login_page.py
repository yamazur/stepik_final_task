from .base_page import BasePage
from .locators import LoginPageLocators, BasketPageLocators, RegisterPageLocators

class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, 'Login page URL is incorrect'

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), 'Login form is not present.'

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTER_FORM), 'Register form is not present.'
        assert True

    def register_new_user(self, email, password):
        email_input = self.browser.find_element(*RegisterPageLocators.EMAIL_INPUT)
        email_input.clear()
        email_input.send_keys(email)

        password_input = self.browser.find_element(*RegisterPageLocators.PASSWORD_INPUT)
        password_input.clear()
        password_input.send_keys(password)

        password_input_confirm = self.browser.find_element(*RegisterPageLocators.PASSWORD_CONFIRM)
        password_input_confirm.clear()
        password_input_confirm.send_keys(password)

        register_button = self.browser.find_element(*RegisterPageLocators.REGISTER_BUTTON)
        register_button.click()