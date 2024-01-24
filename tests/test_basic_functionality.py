import time

import allure

from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper
from pages.order_feed_page import OrderFeedPageHelper


class TestBasicFunctionality:

    @allure.title('Проверка нажатия на ссылку "Конструктор"')
    def test_click_link_constructor(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        main_page.click_on_link_constructor()
        actual_result = main_page.get_text_h1()

        assert driver.current_url == main_page.base_url
        assert actual_result == 'Соберите бургер'

    @allure.title('Проверка нажатия на ссылку "Лента заказов"')
    def test_click_link_order_feed(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        actual_result = order_feed_page.get_text_h1()

        assert '/feed' in driver.current_url
        assert actual_result == 'Лента заказов'

    @allure.title('Проверка открытия модального окна "Детали ингредиента"')
    def test_open_modal_ingredient(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_ingredient()
        actual_result = main_page.get_class_modal_ingredient()

        assert 'Modal_modal_opened__3ISw4' in actual_result

    @allure.title('Проверка закрытия модального окна "Детали ингредиента" кликом на крестик')
    def test_close_modal_ingredient(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_ingredient()
        main_page.click_on_button_close_ingredient()
        actual_result = main_page.get_class_modal_ingredient()

        assert 'Modal_modal_opened__3ISw4' not in actual_result
        assert driver.current_url == main_page.base_url

    @allure.title('Проверка увеличения счетчика при добавления ингредиента в заказ')
    def test_counter_ingredient_bun(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.add_ingredient_to_order()
        actual_result = main_page.get_count_ingredient()

        assert actual_result == '2'

    @allure.title('Проверка создания заказа с добавленными ингредиентами под авторизованным пользователем')
    def test_make_order_authorized_user_with_ingredient(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.add_ingredient_to_order()
        main_page.click_on_button_make_order()
        actual_result = main_page.get_class_modal_order()

        assert 'Modal_modal_opened__3ISw4' in actual_result

    @allure.title('Проверка создания заказа без ингредиентов под авторизованным пользователем')
    def test_make_order_authorized_user_without_ingredient(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        time.sleep(1)
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.click_on_button_make_order()
        actual_result = main_page.get_class_modal_order()

        assert 'Modal_modal_opened__3ISw4' not in actual_result
