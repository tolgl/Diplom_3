from pages.base_page import BasePage
import allure


class TestClickLogo:
    @allure.title('Проверка перехода на страницу восстановления пароля по кнопке "Восстановить пароль"')
    def test_redirection_on_recovery_password_page(self, driver):
        # метод нажатия на логотип "Самокат"
        main_page = BasePage(driver)
        main_page.go_to_page()