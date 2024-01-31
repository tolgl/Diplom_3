# Автотесты для сервиса [Stellar Burgers](https://stellarburgers.nomoreparties.site/)
*В проекте использовался фреймворк Selenium, Pytest и Allure*


1. Файл locators/main_page_locators.py содержит локаторы главной страницы
2. Файл locators/login_page_locators.py содержит локаторы страницы авторизации
3. Файл locators/order_feed_page_locators.py содержит локаторы страницы "Лента заказов"
4. Файл locators/password_recovery_page_locators.py содержит локаторы страницы восстановления пароля
5. Файл locators/personal_account_page_locators.py содержит локаторы страницы ЛК
6. Файл locators/base_page_locators.py содержит локатор лоадера
7. Файл pages/base_page.py содержит методы:
   - __go_to_page__ - открытие главной страницы сервиса
   - __find_element__ - поиск элемента через ожидание видимости
   - __wait_clickable_element__ - поиск элемента через ожидание кликабельности
   - __wait_change_url__ - ожидание смены url
   - __wait_hidden_loader__ - ожидание скрытия лоадера
8. Файл pages/main_page.py содержит методы:
   - __click_on_button_personal_account__ - нажимает на ссылку "Личный кабинет" в шапке
   - __click_on_link_constructor__ - нажимает на ссылку "Конструктор" в шапке
   - __get_text_h1__ - получает заголовок главной страницы
   - __click_on_link_order_feed__ - нажимает на ссылку "Лента заказов" в шапке
   - __click_on_ingredient__ - нажимает на первый ингредиент
   - __get_class_modal_ingredient__ - получает класс модального окна "Детали ингредиента"
   - __click_on_button_close_ingredient__ - закрывает модальное окно "Детали ингредиента"
   - __add_ingredient_to_order__ - добавляет ингредиент в заказ
   - __get_count_ingredient__ - получает количество ингредиента в заказе
   - __click_on_button_make_order__ - нажимает на кнопку "Оформить заказ"
   - __get_class_modal_order__ - получает класс модального окна созданного заказа
   - __click_on_button_close_modal_order__ - закрывает модальное окно созданного заказа
   - __get_number_order_in_modal_order__ - получает номер заказа в модальном окне созданного заказа
9. Файл pages/login_page.py содержит методы:
   - __click_on_button_recovery_password__ - нажимает на ссылку "Восстановить пароль"
   - __filling_field_email_on_login_page__ - заполняет поле email на странице авторизации
   - __filling_field_password_on_login_page__ - заполняет поле пароль на странице авторизации
   - __click_on_button_login__ - нажимает на кнопку "Войти"
   - __get_text_h2__ - получает заголовок страницы авторизации
10. Файл pages/order_feed_page.py содержит методы:
    - __get_text_h1__ - получает заголовок страницы
    - __click_first_order__ - нажимает на первый заказ
    - __get_class_modal_details__ - получает класс модального окна заказа
    - __get_number_order_in_order_feed__ - получает номер заказ в ленте заказов
    - __get_count_order_in_order_feed_for_all_time__ - получает количество заказов за все время
    - __get_count_order_in_order_feed_for_current_day__ - получает количество заказов за текущий день
    - __get_order_in_work__ - получает номер заказа на блоке "В работе"
11. Файл pages/password_recovery_page.py содержит методы:
    - __get_h2_password_recovery__ - получает заголовок страницы
    - __filling_email__ - заполняет поле email
    - __click_button_confirm_password_recovery__ - нажимает на кнопку "Восстановить"
    - __find_button_save_new_password__ - получает текст кнопки "Сохранить"
    - __click_field_new_password__ - нажимает на поле нового пароля
    - __get_class_field_new_password__ - получает класс поля ввода нового пароля
12. Файл pages/personal_account_page.py содержит методы:
    - __get_text_link_history_orders__ - получает текст ссылки "История заказов"
    - __click_link_history_orders__ - нажимает на ссылку "История заказов"
    - __click_button_logout__ - нажимает на кнопку "Выход"
    - __get_number_order_in_history_order__ - получает номер заказа в истории заказов
13. Файл tests/conftest содержит фикстуры:
    - __driver__ - фикстура инициальзации драйвера в двух браузерах Chrome и Firefox
    - __creating_new_user__ - создает и удаляет нового пользователя по api 
14. Файл tests/test_basic_functionality.py содержит автотесты:
    - __test_click_link_constructor__ - проверяет нажатие на ссылку "Конструктор"
    - __test_click_link_order_feed__ - проверяет нажатие на ссылку "Лента Заказов"
    - __test_open_modal_ingredient__ - проверяет открытие модального окна с ингредиентом
    - __test_close_modal_ingredient__ - закрывает модальное окно с ингредиентом
    - __test_counter_ingredient_bun__ - проверяет что при добавлении ингредиента в заказ увеличивается счетчик
    - __test_make_order_authorized_user_with_ingredient__ - проверяет создание заказа под авторизованным пользователем с добавленным ингредиентом
    - __test_make_order_authorized_user_without_ingredient__ - проверяет создание заказа под авторизованным пользователем без добавления ингредиента
15. Файл tests/test_order_feed.py содержит автотесты:
    - __test_open_modal_order_details__ - проверяет открытие модального окна с детальной информацией о заказе
    - __test_check_order_user_in_order_feed__ - проверяет что созданный заказ пользователя есть в ленте заказов
    - __test_increasing_counter_order_for_all_time__ - проверяет увеличение счетчика "Выполнено за все время" при создании заказа
    - __test_increasing_counter_order_for_current_day__ - проверяет увеличение счетчика "Выполнено за сегодня" при создании заказа
    - __test_check_order_on_block_in_work__ - проверяет отображение созданного заказа на блоке "В работе"
16. Файл tests/test_password_recovery.py содержит автотесты:
    - __test_redirection_on_recovery_password_page__ - проверяет переход на страницу "Восстановление пароля"
    - __test_password_recovery_with_filled_email__ - проверяет переход на страницу ввода нового пароля
    - __test_check_activity_field_new_password__ - проверяет изменение класса при нажатии на поле "Пароль"
17. Файл tests/test_personal_account.py содержит автотесты:
    - __test_redirection_on_personal_account_page__ - проверяет переход на страницу ЛК
    - __test_redirection_on_history_orders_page__ - проверяет переход на страницу ЛК в историю заказов
    - __test_logout_personal_account__ - проверяет разлогинивание пользователя
18. Файл test_data.py генерирует имя, почту и пароль для пользователя
19. Файл requirements.txt содержит используемые библиотеки в проекте. Для установки всех зависимостей необходимо выполнить команду pip3 install -r requirements.txt