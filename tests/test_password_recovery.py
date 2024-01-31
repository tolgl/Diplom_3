import allure

from pages.base_page import BasePage
from pages.main_page import MainPageHelper
from pages.login_page import LoginPageHelper
from pages.password_recovery_page import PasswordRecoveryPageHelper


class TestPasswordRecovery:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_redirection_on_recovery_password_page(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.click_on_button_recovery_password()
        password_recovery_page = PasswordRecoveryPageHelper(driver)
        actual_result = password_recovery_page.get_h2_password_recovery()
        base_page = BasePage(driver)
        current_url = base_page.get_current_url()

        assert 'forgot-password' in current_url
        assert actual_result == 'Восстановление пароля'

    @allure.title('Проверка нажатия на кнопку "Восстановить" с введенным email')
    def test_password_recovery_with_filled_email(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.click_on_button_recovery_password()
        login_page.wait_hidden_loader()
        password_recovery_page = PasswordRecoveryPageHelper(driver)
        password_recovery_page.filling_email('test@test.ru')
        password_recovery_page.click_button_confirm_password_recovery()
        actual_result = password_recovery_page.find_button_save_new_password()
        base_page = BasePage(driver)
        current_url = base_page.get_current_url()

        assert 'reset-password' in current_url
        assert actual_result == 'Сохранить'

    @allure.title('Проверка активности поля "Пароль"')
    def test_check_activity_field_new_password(self, driver):
        main_page = MainPageHelper(driver)
        main_page.go_to_page()
        main_page.wait_hidden_loader()
        main_page.click_on_button_personal_account()
        login_page = LoginPageHelper(driver)
        login_page.click_on_button_recovery_password()
        login_page.wait_hidden_loader()
        password_recovery_page = PasswordRecoveryPageHelper(driver)
        password_recovery_page.filling_email('test@test.ru')
        password_recovery_page.click_button_confirm_password_recovery()
        password_recovery_page.wait_hidden_loader()
        password_recovery_page.click_field_new_password()
        actual_result = password_recovery_page.get_class_field_new_password()

        assert 'input__placeholder-focused' in actual_result
