from locators.order_feed_page_locators import OrderFeedPageLocators
from pages.base_page import BasePage

import allure


class OrderFeedPageHelper(BasePage):

    @allure.step('Получаем заголовок страницы "Лента заказов"')
    def get_text_h1(self):
        return self.find_element(OrderFeedPageLocators.h1, wait_time=5).text
