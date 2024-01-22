from selenium.webdriver.common.by import By


class PersonalAccountPageLocators:
    link_history_orders = (By.XPATH, ".//a[@href='/account/order-history']")
    button_logout = (By.XPATH, './/button[text()="Выход"]')
