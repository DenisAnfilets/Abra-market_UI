from pages.forgot_password_page import ForgotPasswordPage
from pages.main_page import MainPage


def test_reset_password(browser):
    link = 'https://www.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_icon_button()
    page.go_to_login()
    link = 'https://www.abra-market.com/forgotPassword'
    page = ForgotPasswordPage(browser, link)
    page.open()
    page.go_to_email()
    page.go_to_reset_password()
