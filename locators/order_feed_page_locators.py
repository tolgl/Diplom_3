from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    h1 = (By.XPATH, ".//h1[text()='Лента заказов']")
    first_order = (By.XPATH, ".//div/ul/li[1]/a")
    modal_order_details = (By.XPATH, ".//p[text()='Выполнен']/parent::div/parent::div/parent::section")
    number_order = (By.XPATH, "//ul/li[1]/a/div[1]/p[1]")
    count_order_for_all_time = (By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[2]")
    count_order_for_current_day = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[2]")
    order_in_work = (By.XPATH, ".//p[text()='В работе:']/parent::div/ul[2]/li")
