from selenium.webdriver.common.by import By


class RegistrationPageLocators:
    field_name = (By.XPATH, ".//fieldset[1]//input")
    field_email = (By.XPATH, ".//fieldset[2]//input")
    field_password = (By.XPATH, ".//fieldset[3]//input")
    button_registration = (By.XPATH, ".//button[text() = 'Зарегистрироваться']")
