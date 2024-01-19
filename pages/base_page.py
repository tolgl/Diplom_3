import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.base_url = 'https://stellarburgers.nomoreparties.site/'

    @allure.step('Открытие страницы Stellar Burgers')
    def go_to_page(self):
        return self.driver.get(self.base_url)

    def find_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.visibility_of_element_located(locator))
