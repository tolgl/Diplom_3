import allure
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper
from pages.personal_account_page import PersonalAccountPageHelper


class TestPersonalAccount:

    @allure.title('Проверка перехода на страницу "Личный кабинет"')
    def test_redirection_on_personal_account_page(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        personal_account_page = PersonalAccountPageHelper(driver)
        actual_result = personal_account_page.get_text_link_history_orders()

        assert 'account/profile' in driver.current_url
        assert actual_result == 'История заказов'

    @allure.title('Проверка перехода на страницу "История заказов"')
    def test_redirection_on_history_orders_page(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        personal_account_page = PersonalAccountPageHelper(driver)
        personal_account_page.wait_hidden_loader()
        personal_account_page.click_link_history_orders()

        assert 'account/order-history' in driver.current_url

    @allure.title('Проверка выхода из ЛК')
    def test_logout_personal_account(self, driver, creating_new_user):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.filling_field_email_on_login_page(email=creating_new_user[0])
        login_page.filling_field_password_on_login_page(password=creating_new_user[1])
        login_page.click_on_button_login()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        personal_account_page = PersonalAccountPageHelper(driver)
        personal_account_page.wait_hidden_loader()
        personal_account_page.click_button_logout()
        actual_result = login_page.get_text_h2()

        assert 'login' in driver.current_url
        assert actual_result == 'Вход'
