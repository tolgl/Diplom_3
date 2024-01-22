from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage

import allure


class MainPageHelper(BasePage):

    @allure.step('Нажимаем на кнопку "Личный кабинет"')
    def click_on_button_personal_account(self):
        self.wait_clickable_element(MainPageLocators.button_personal_account, wait_time=5).click()

    @allure.step('Нажимаем на ссылку "Конструктор"')
    def click_on_link_constructor(self):
        self.wait_clickable_element(MainPageLocators.link_constructor, wait_time=5).click()

    @allure.step('Получаем заголовок главной страницы')
    def get_text_h1(self):
        return self.find_element(MainPageLocators.h1, wait_time=5).text

    @allure.step('Нажимаем на ссылку "Лента заказов"')
    def click_on_link_order_feed(self):
        self.wait_clickable_element(MainPageLocators.link_order_feed, wait_time=5).click()
