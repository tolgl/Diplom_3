import time

import allure
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper
from pages.personal_account_page import PersonalAccountPageHelper
from pages.registration_page import RegistrationPageHelper


class TestPersonalAccount:

    @allure.title('Проверка перехода на страницу "Личный кабинет"')
    def test_redirection_on_personal_account_page(self, driver, generation_user_data):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.click_link_registration()
        registration_page = RegistrationPageHelper(driver)
        registration_page.filling_field_name(name=generation_user_data[0])
        registration_page.filling_field_email(email=generation_user_data[1])
        registration_page.filling_field_password(password=generation_user_data[2])
        registration_page.click_on_button_registration()
        login_page.filling_field_email_on_login_page(email=generation_user_data[1])
        login_page.filling_field_password_on_login_page(password=generation_user_data[2])
        login_page.click_on_button_login()
        main_page.click_on_button_personal_account()
        personal_account_page = PersonalAccountPageHelper(driver)
        actual_result = personal_account_page.gey_text_link_history_orders()

        assert 'account/profile' in driver.current_url
        assert actual_result == 'История заказов'
