from locators.main_page_locators import MainPageLocators
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

import allure


class LoginPageHelper(BasePage):

    @allure.step('Нажатие на кнопку "Восстановить пароль"')
    def click_on_button_recovery_password(self):
        self.wait_clickable_element(LoginPageLocators.button_password_recovery, wait_time=5).click()

    @allure.step('Получение текста "Восстановить пароль"')
    def get_h2_password_recovery(self):
        return self.find_element(LoginPageLocators.h2_password_recovery, wait_time=3).text
