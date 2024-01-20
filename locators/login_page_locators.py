from selenium.webdriver.common.by import By


class LoginPageLocators:
    button_password_recovery = (By.XPATH, ".//a[@href='/forgot-password']")
