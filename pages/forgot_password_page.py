from .locators import ForgotPasswordPageLocators
from .base_page import BasePage
import time


class ForgotPasswordPage(BasePage):
    def go_to_email(self):
        email_fpp = self.browser.find_element(*ForgotPasswordPageLocators.EMAIL_FPP)
        email_fpp.send_keys('dude78@yopmail.com')
        time.sleep(2)

    def go_to_reset_password(self):
        reset_password_button = self.browser.find_element(*ForgotPasswordPageLocators.RESET_PASSWORD_BUTTON)
        reset_password_button.click()
