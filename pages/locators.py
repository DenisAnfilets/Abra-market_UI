from selenium.webdriver.common.by import By


class MainPageLocators:
    ICON_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/button')
    REGISTRATION = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/ul/li[2]/a')
    LOGIN = (By.XPATH, '//*[@id="root"]/div/div/header/div/div[1]/div[4]/div/ul/li[1]/a')


class AuthPageLocators:
    SIGN_UP = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/button[2]')
    LOG_IN = (By.XPATH, '//*[@id="root"]/div/div/main/div[2]/button[1]')
    I_HERE_SELL = (By.XPATH, '//*[@id="root"]/div/div/main/div[3]/button[2]')
    EMAIL_FIELD = (By.XPATH, '//*[@id="root"]/div/div/main/form/div[1]/input')
    PASSWORD_FIELD = (By.XPATH, '//*[@id="root"]/div/div/main/form/div[2]/div[1]/input')
    PASSWORD_FIELD_LOGIN = (By.XPATH, '//*[@id="root"]/div/div/main/form/div[2]/input')
    CONTINUE_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/main/form/button')
    FORGOT_PASSWORD = (By.XPATH, '//*[@id="root"]/div/div/main/div[3]/a')


class ForgotPasswordPageLocators:
    EMAIL_FPP = (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/div/input')
    RESET_PASSWORD_BUTTON = (By.XPATH, '//*[@id="root"]/div/div/div[3]/form/button')
