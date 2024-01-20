from locators.password_recovery_locators import PasswordRecoveryPageLocators
from pages.base_page import BasePage

import allure


class PasswordRecoveryPageHelper(BasePage):

    @allure.step('Получение текста "Восстановить пароль"')
    def get_h2_password_recovery(self):
        return self.find_element(PasswordRecoveryPageLocators.h2_password_recovery, wait_time=3).text

    @allure.step('Заполняем поле "Email"')
    def filling_email(self, email):
        self.find_element(PasswordRecoveryPageLocators.field_email, wait_time=3).send_keys(email)

    @allure.step('Нажимаем на кнопку "Восстановить"')
    def click_button_confirm_password_recovery(self):
        self.wait_clickable_element(PasswordRecoveryPageLocators.button_confirm_password_recovery, wait_time=3).click()

    @allure.step('Ищем кнопку "Сохранить"')
    def find_button_save_new_password(self):
        return self.find_element(PasswordRecoveryPageLocators.button_save_new_password, wait_time=3).text

    @allure.step('Клик на поле "Пароль"')
    def click_field_new_password(self):
        self.wait_clickable_element(PasswordRecoveryPageLocators.field_new_password, wait_time=3).click()

    @allure.step('Получение класса поля "Пароль"')
    def get_class_field_new_password(self):
        return self.find_element(PasswordRecoveryPageLocators.field_new_password, wait_time=3).get_attribute('class')
