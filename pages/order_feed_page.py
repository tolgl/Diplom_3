from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage

import allure


class OrderFeedPageHelper(BasePage):

    @allure.step('Получаем заголовок страницы "Лента заказов"')
    def get_text_h1(self):
        return self.find_element(OrderFeedPageLocators.h1, wait_time=5).text

    @allure.step('Нажимаем на первый заказ в ленте')
    def click_first_order(self):
        self.find_element(OrderFeedPageLocators.first_order, wait_time=5).click()

    @allure.step('Получаем класс модального окна с деталями заказа')
    def get_class_modal_details(self):
        return self.find_element(OrderFeedPageLocators.modal_order_details, wait_time=5).get_attribute('class')

    @allure.step('Получаем номера заказа в ленте заказов')
    def get_number_order_in_order_feed(self):
        return self.find_element(OrderFeedPageLocators.number_order, wait_time=5).text

    @allure.step('Получаем общее количество заказов в ленте заказов')
    def get_count_order_in_order_feed_for_all_time(self):
        return self.find_element(OrderFeedPageLocators.count_order_for_all_time, wait_time=5).text

    @allure.step('Получаем количество заказов за текущий день в ленте заказов')
    def get_count_order_in_order_feed_for_current_day(self):
        return self.find_element(OrderFeedPageLocators.count_order_for_current_day, wait_time=5).text

    @allure.step('Получаем заказ на блоке "В работе" в ленте заказов')
    def get_order_in_work(self):
        return self.find_element(OrderFeedPageLocators.order_in_work, wait_time=5).text
