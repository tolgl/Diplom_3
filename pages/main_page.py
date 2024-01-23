from locators.main_page_locators import MainPageLocators
from pages.base_page import BasePage
from selenium.webdriver import ActionChains

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

    @allure.step('Нажимаем на ингредиент')
    def click_on_ingredient(self):
        self.wait_clickable_element(MainPageLocators.first_ingredient_bun, wait_time=5).click()

    @allure.step('Получаем класс модального окна "Детали ингредиента"')
    def get_class_modal_ingredient(self):
        return self.find_element(MainPageLocators.modal_ingredient, wait_time=3).get_attribute('class')

    @allure.step('Закрываем модальное окно кликом по крестику')
    def click_on_button_close_ingredient(self):
        self.find_element(MainPageLocators.button_close_modal_ingredient, wait_time=5).click()

    @allure.step('Добавляем ингредиент в заказ')
    def add_ingredient_to_order(self):
        draggable = self.find_element(MainPageLocators.first_ingredient_bun, wait_time=5)
        droppable = self.find_element(MainPageLocators.burger_constructor, wait_time=5)
        ActionChains(self.driver) \
            .drag_and_drop(draggable, droppable) \
            .perform()

    @allure.step('Получаем количество ингредиента')
    def get_count_ingredient(self):
        return self.find_element(MainPageLocators.ingredient_counter, wait_time=3).text

    @allure.step('Нажимаем на кнопку "Оформить заказ"')
    def click_on_button_make_order(self):
        self.find_element(MainPageLocators.button_make_order, wait_time=5).click()

    @allure.step('Получаем класс модального окна оформленного заказа')
    def get_class_modal_order(self):
        return self.find_element(MainPageLocators.modal_order, wait_time=3).get_attribute('class')
