from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

import allure


class MainPageHelper(BasePage):

    @allure.step('Нажатие на кнопку "Личный кабинет"')
    def click_on_button_personal_account(self):
        self.wait_clickable_element(MainPageLocators.button_personal_account, wait_time=5).click()
