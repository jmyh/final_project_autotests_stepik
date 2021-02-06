from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        assert "login" in self.browser.current_url, "Login url is not correct"

    def should_be_login_form(self):
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_FORM), "Registration form is not presented"

    def should_be_re_login_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_LOGIN_FIELD), "Login field in registration " \
                                                                                     "form is not presented "

    def should_be_re_password_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD), "Password field in " \
                                                                                        "registration form is not " \
                                                                                        "presented "

    def should_be_re_confirm_password_field(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD), "Field for password " \
                                                                                                "confirmation in " \
                                                                                                "registration form is " \
                                                                                                "not presented "

    def should_be_register_btn(self):
        assert self.is_element_present(*LoginPageLocators.REGISTRATION_BTN), "Registration's button is not presented"

    def register_new_user(self, email, password):
        self.should_be_re_login_field()
        login_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_LOGIN_FIELD)
        login_field.send_keys(email)
        self.should_be_re_password_field()
        password_field=self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_FIELD)
        password_field.send_keys(password)
        self.should_be_re_confirm_password_field()
        password_field = self.browser.find_element(*LoginPageLocators.REGISTRATION_CONFIRM_PASSWORD_FIELD)
        password_field.send_keys(password)
        self.should_be_register_btn()
        login_btn=self.browser.find_element(*LoginPageLocators.REGISTRATION_BTN)
        login_btn.click()

