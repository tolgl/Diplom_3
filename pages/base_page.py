import allure
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from locators.base_page_locators import BasePageLocators


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

    def wait_clickable_element(self, locator, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.element_to_be_clickable(locator))

    def wait_change_url(self, url_contains, wait_time=10):
        return WebDriverWait(self.driver, wait_time).until(
            expected_conditions.url_contains(url_contains))

    def wait_hidden_loader(self):
        return WebDriverWait(self.driver, 5).until(
            expected_conditions.invisibility_of_element(BasePageLocators.loader))

    def get_current_url(self):
        return self.driver.current_url
