from selenium.webdriver.common.by import By


class PasswordRecoveryPageLocators:
    h2_password_recovery = (By.XPATH, ".//h2[text()='Восстановление пароля']")
    field_email = (By.NAME, "name")
    button_confirm_password_recovery = (By.XPATH, ".//button[text()='Восстановить']")
    button_save_new_password = (By.XPATH, ".//button[text()='Сохранить']")
    field_new_password = (By.XPATH, ".//input[@name='Введите новый пароль']/parent::div/label")
