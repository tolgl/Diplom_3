from selenium.webdriver.common.by import By


class MainPageLocators:
    button_personal_account = (By.XPATH, ".//a[@href='/account']")
    link_constructor = (By.XPATH, ".//p[text()='Конструктор']//parent::a")
    h1 = (By.XPATH, ".//h1[text()='Соберите бургер']")
    link_order_feed = (By.XPATH, ".//a[@href='/feed']")
    first_ingredient_bun = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']")
    modal_ingredient = (By.XPATH, ".//h2[text()='Детали ингредиента']/parent::div/parent::div/parent::section")
    button_close_modal_ingredient = (By.XPATH, ".//section[1]/div[1]/button")
    burger_constructor = (By.CLASS_NAME, "BurgerConstructor_basket__list__l9dp_")
    ingredient_counter = (By.XPATH, ".//a[@href='/ingredient/61c0c5a71d1f82001bdaaa6d']//p")
    button_make_order = (By.XPATH, ".//button[text()='Оформить заказ']")
    modal_order = (By.XPATH, ".//p[text()='идентификатор заказа']/parent::div/parent::div/parent::section")
    button_close_modal_order = (By.XPATH, ".//section[1]/div[1]/button")
    number_order = (By.XPATH, ".//p[text()='идентификатор заказа']/parent::div/h2")
