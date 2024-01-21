from selenium.webdriver.common.by import By


class LoginPageLocators:
    button_password_recovery = (By.XPATH, ".//a[@href='/forgot-password']")
    link_registration = (By.XPATH, ".//a[@href='/register']")
    field_email = (By.XPATH, "//input[@name='name']")
    field_password = (By.XPATH, "//input[@name='Пароль']")
    button_login = (By.XPATH, ".//button[text() = 'Войти']")
