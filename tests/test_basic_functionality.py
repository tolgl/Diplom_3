import time

import allure
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper
from pages.personal_account_page import PersonalAccountPageHelper
from pages.registration_page import RegistrationPageHelper


class TestPersonalAccount:

    @allure.title('Проверка нажатия на ссылку "Конструктор"')
    def test_click_link_constructor(self, driver, generation_user_data):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.click_on_button_personal_account()
        main_page.click_on_link_constructor()
        actual_result = main_page.get_text_h1()

        assert driver.current_url == main_page.base_url
        assert actual_result == 'Соберите бургер'
