from selenium.webdriver.common.by import By


class OrderFeedPageLocators:
    h1 = (By.XPATH, ".//h1[text()='Лента заказов']")
    first_order = (By.CLASS_NAME, "OrderHistory_link__1iNby")
    modal_order_details = (By.XPATH, ".//p[text()='Выполнен']/parent::div/parent::div/parent::section")
    number_order = (By.XPATH, ".//p[contains(text(), '#')]")
    count_order_for_all_time = (By.XPATH, ".//p[text()='Выполнено за все время:']/parent::div/p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    count_order_for_current_day = (By.XPATH, ".//p[text()='Выполнено за сегодня:']/parent::div/p[contains(@class, 'OrderFeed_number__2MbrQ')]")
    order_in_work = (By.XPATH, ".//ul[contains(@class, 'OrderFeed_orderListReady__1YFem')]/li[not(contains(text(), 'Все текущие заказы готовы!'))]")
