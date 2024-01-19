import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.firefox.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.firefox import GeckoDriverManager


@pytest.fixture(params=['firefox', 'chrome'])
def driver(request):
    if request.param == 'firefox':
        firefox_driver = GeckoDriverManager().install()
        service = Service(firefox_driver)
        driver = webdriver.Firefox(service=service)
    if request.param == 'chrome':
        chrome_driver = ChromeDriverManager().install()
        service = Service(chrome_driver)
        options = Options()
        options.add_argument("--window-size=1920,1080")
        driver = webdriver.Chrome(service=service, options=options)

    yield driver
    driver.quit()
