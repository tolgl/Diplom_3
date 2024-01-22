from selenium.webdriver.common.by import By


class MainPageLocators:
    button_personal_account = (By.XPATH, ".//a[@href='/account']")
    link_constructor = (By.XPATH, ".//p[text()='Конструктор']//parent::a")
    h1 = (By.XPATH, ".//h1[text()='Соберите бургер']")
    link_order_feed = (By.XPATH, ".//a[@href='/feed']")
