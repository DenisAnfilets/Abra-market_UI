from .base_page import BasePage
from .locators import AuthPageLocators
import time


class AuthPage(BasePage):
    def go_to_sign_up(self):
        sign_up = self.browser.find_element(*AuthPageLocators.SIGN_UP)
        sign_up.click()

    def go_to_i_here_sell(self):
        i_here_sell = self.browser.find_element(*AuthPageLocators.I_HERE_SELL)
        i_here_sell.click()

    def go_to_email(self):
        login_email = self.browser.find_element(*AuthPageLocators.EMAIL_FIELD)
        login_email.send_keys('dude78@yopmail.com')
        time.sleep(1)

    def go_to_password(self):
        login_password = self.browser.find_element(*AuthPageLocators.PASSWORD_FIELD)
        login_password.send_keys('duDe+78!')
        time.sleep(1)

    def go_to_continue_button(self):
        continue_button = self.browser.find_element(*AuthPageLocators.CONTINUE_BUTTON)
        continue_button.click()

    def go_to_password_login(self):
        login_password = self.browser.find_element(*AuthPageLocators.PASSWORD_FIELD_LOGIN)
        login_password.send_keys('duDe+78!')
        time.sleep(1)
