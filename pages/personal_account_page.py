from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage

import allure


class PersonalAccountPageHelper(BasePage):

    @allure.step('Получаем текст "История заказов" в ЛК')
    def get_text_link_history_orders(self):
        return self.find_element(PersonalAccountPageLocators.link_history_orders, wait_time=5).text

    @allure.step('Нажимаем на ссылку "История заказов" в ЛК')
    def click_link_history_orders(self):
        self.find_element(PersonalAccountPageLocators.link_history_orders, wait_time=5).click()

    @allure.step('Нажимаем на кнопку "Выход" в ЛК')
    def click_button_logout(self):
        self.find_element(PersonalAccountPageLocators.button_logout, wait_time=5).click()
