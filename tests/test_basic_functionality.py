import allure
from pages.main_page import MainPageHelper
from pages.order_feed_page import OrderFeedPageHelper


class TestBasicFunctionality:

    @allure.title('Проверка нажатия на ссылку "Конструктор"')
    def test_click_link_constructor(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_on_button_personal_account()
        main_page.click_on_link_constructor()
        actual_result = main_page.get_text_h1()

        assert driver.current_url == main_page.base_url
        assert actual_result == 'Соберите бургер'

    @allure.title('Проверка нажатия на ссылку "Лента заказов"')
    def test_click_link_order_feed(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        actual_result = order_feed_page.get_text_h1()

        assert '/feed' in driver.current_url
        assert actual_result == 'Лента заказов'
