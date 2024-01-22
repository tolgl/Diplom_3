from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

import allure


class LoginPageHelper(BasePage):

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_button_recovery_password(self):
        self.wait_clickable_element(LoginPageLocators.button_password_recovery, wait_time=5).click()

    @allure.step('Нажатие на ccылку "Зарегистрироваться"')
    def click_link_registration(self):
        self.wait_clickable_element(LoginPageLocators.link_registration, wait_time=3).click()

    @allure.step('Заполняем поле "Email" на странице авторизации')
    def filling_field_email_on_login_page(self, email):
        self.wait_change_url(url_contains='login')
        self.find_element(LoginPageLocators.field_email, wait_time=5).send_keys(email)

    @allure.step('Заполняем поле "Пароль" на странице авторизации')
    def filling_field_password_on_login_page(self, password):
        self.find_element(LoginPageLocators.field_password, wait_time=5).send_keys(password)

    @allure.step('Нажимаем на кнопку "Войти" на странице авторизации')
    def click_on_button_login(self):
        self.wait_clickable_element(LoginPageLocators.button_login, wait_time=5).click()

    @allure.step('Получаем текст заголовка "Вход"')
    def get_text_h2(self):
        return self.find_element(LoginPageLocators.h2, wait_time=5).text
