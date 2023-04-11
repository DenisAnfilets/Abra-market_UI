from pages.main_page import MainPage


def test_registration_seller(browser):
    """ Function to go to authorization page for registration"""
    link = 'https://www.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_icon_button()
    page.go_to_registration()


def test_login(browser):
    """ Function to go to authorization page for login"""
    link = 'https://www.abra-market.com/'
    page = MainPage(browser, link)
    page.open()
    page.go_to_icon_button()
    page.go_to_login()
