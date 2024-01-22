import json
import pytest
import requests
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from test_data import generate_random_string


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        driver = webdriver.Firefox()
        driver.maximize_window()
    else:
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(options=options)

    yield driver
    driver.quit()


@pytest.fixture()
def creating_new_user():

    login_pass = []
    # генерируем емаил, пароль и имя пользователя
    email = f'{generate_random_string(7)}@mail.ru'
    password = generate_random_string(6)
    name = generate_random_string(6)

    # собираем тело запроса
    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    # отправляем запрос на создание пользователя
    response = requests.post(url='https://stellarburgers.nomoreparties.site/api/auth/register',
                             data=json.dumps(payload),
                             headers={"Content-type": "application/json"})

    login_pass.append(email)
    login_pass.append(password)

    yield login_pass

    # удаляем пользователя после выполнения теста
    requests.delete(url='https://stellarburgers.nomoreparties.site/api/auth/user',
                    headers={"Authorization": response.json()['accessToken']})
