from pages.auth_page import AuthPage
from pages.main_page import MainPage


def test_registration_seller(browser):
    """ Function for create seller with required fields"""
    link = 'https://www.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_icon_button()
    page.go_to_registration()
    link = 'https://www.abra-market.com/auth'
    page = AuthPage(browser, link)
    page.open()
    page.go_to_sign_up()
    page.go_to_email()
    page.go_to_password()
    page.go_to_continue_button()


def test_login(browser):
    """ Function for login with required fields"""
    link = 'https://www.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_icon_button()
    page.go_to_login()
    link = 'https://www.abra-market.com/auth'
    page = AuthPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_password_login()
    page.go_to_continue_button()
