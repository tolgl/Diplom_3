import time

import allure

from pages.login_page import LoginPageHelper
from pages.main_page import MainPageHelper
from pages.order_feed_page import OrderFeedPageHelper
from pages.personal_account_page import PersonalAccountPageHelper


class TestOrderFeed:

    @allure.title('Проверка открытия окна с деталями заказа')
    def test_open_modal_order_details(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        order_feed_page.click_first_order()
        actual_result = order_feed_page.get_class_modal_details()

        assert 'Modal_modal_opened__3ISw4' in actual_result

    @allure.title('Проверка заказов пользователя в "Лента заказов"')
    def test_check_order_user_in_order_feed(self, driver, creating_new_user):
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
        main_page.wait_hidden_loader()
        main_page.click_on_button_close_modal_order()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        personal_account_page = PersonalAccountPageHelper(driver)
        personal_account_page.wait_hidden_loader()
        personal_account_page.click_link_history_orders()
        expected_result = personal_account_page.get_number_order_in_history_order()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        order_feed_page.wait_hidden_loader()
        actual_result = order_feed_page.get_number_order_in_order_feed()

        assert actual_result == expected_result

    @allure.title('Проверка увеличения счетчика "Выполнено за все время" в ленте заказов')
    def test_increasing_counter_order_for_all_time(self, driver, creating_new_user):
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
        time.sleep(2)
        expected_result = main_page.get_number_order_in_modal_order()
        main_page.click_on_button_close_modal_order()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        actual_result = order_feed_page.get_count_order_in_order_feed_for_all_time()

        assert actual_result == expected_result

    @allure.title('Проверка увеличения счетчика "Выполнено за сегодня" в ленте заказов')
    def test_increasing_counter_order_for_current_day(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        order_feed_page = OrderFeedPageHelper(driver)
        count_before_make_order = order_feed_page.get_count_order_in_order_feed_for_current_day()
        main_page.click_on_link_constructor()
        main_page.add_ingredient_to_order()
        main_page.click_on_button_make_order()
        main_page.click_on_button_close_modal_order()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        count_after_make_order = order_feed_page.get_count_order_in_order_feed_for_current_day()

        assert int(count_after_make_order) == int(count_before_make_order) + 1

    @allure.title('Проверка отображения заказа в ленте заказов на блоке "В работе"')
    def test_check_order_on_block_in_work(self, driver, creating_new_user):
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
        time.sleep(2)
        expected_result = main_page.get_number_order_in_modal_order()
        main_page.click_on_button_close_modal_order()
        main_page.wait_hidden_loader()
        main_page.click_on_link_order_feed()
        time.sleep(3)
        order_feed_page = OrderFeedPageHelper(driver)
        actual_result = order_feed_page.get_order_in_work()

        assert actual_result == f'0{expected_result}'
