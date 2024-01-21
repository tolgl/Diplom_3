from locators.personal_account_page_locators import PersonalAccountPageLocators
from pages.base_page import BasePage

import allure


class PersonalAccountPageHelper(BasePage):

    @allure.step('Получаем текст "История заказа" в ЛК')
    def gey_text_link_history_orders(self):
        return self.find_element(PersonalAccountPageLocators.link_history_orders, wait_time=5).text
