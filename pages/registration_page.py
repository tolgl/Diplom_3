from locators.registration_page_locators import RegistrationPageLocators
from pages.base_page import BasePage

import allure


class RegistrationPageHelper(BasePage):

    @allure.step('Заполнение поля "Имя"')
    def filling_field_name(self, name):
        self.find_element(RegistrationPageLocators.field_name, wait_time=5).send_keys(name)

    @allure.step('Заполняем поле "Email" на странице регистрации')
    def filling_field_email(self, email):
        self.find_element(RegistrationPageLocators.field_email, wait_time=5).send_keys(email)

    @allure.step('Заполняем поле "Пароль" на странице регистрации')
    def filling_field_password(self, password):
        self.find_element(RegistrationPageLocators.field_password, wait_time=5).send_keys(password)

    @allure.step('Нажимаем на кнопку "Зарегистрироваться"')
    def click_on_button_registration(self):
        self.wait_clickable_element(RegistrationPageLocators.button_registration, wait_time=5).click()
