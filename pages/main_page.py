from .locators import MainPageLocators
from .base_page import BasePage
import time


class MainPage(BasePage):
    def go_to_icon_button(self):
        icon_button = self.browser.find_element(*MainPageLocators.ICON_BUTTON)
        icon_button.click()
        time.sleep(3)

    def go_to_registration(self):
        registration = self.browser.find_element(*MainPageLocators.REGISTRATION)
        registration.click()

    def go_to_login(self):
        login = self.browser.find_element(*MainPageLocators.LOGIN)
        login.click()
