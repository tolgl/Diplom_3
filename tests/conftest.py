import pytest
import random
import string
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


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
def generation_user_data():
    domain = ['ya.ru', 'gmail.com', 'bk.ru']
    random_login = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(3, 10)))
    random_domain = random.choice(domain)
    name = ''.join(random.choices(string.ascii_lowercase, k=random.randint(3, 10)))
    email = f'{random_login}@{random_domain}'
    password = ''.join(random.choices(string.ascii_lowercase + string.digits, k=random.randint(6, 10)))

    return [name, email, password]
