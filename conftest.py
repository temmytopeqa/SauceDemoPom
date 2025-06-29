import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from ActionPage.login_page import LoginPage
from ActionPage.add_to_cart import AddToCartPage
from ActionPage.payment_page import PaymentPage
from ActionPage.logout_page import LogoutPage
from Config.configuration import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    chrome_options.add_argument("--disable-gpu")
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    login_page = LoginPage(driver_setup)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

@pytest.fixture(scope="module")
def add_to_cart(driver_setup):
    return AddToCartPage(driver_setup)

@pytest.fixture(scope="module")
def payment(driver_setup):
    return PaymentPage(driver_setup)

@pytest.fixture(scope="module")
def logout(driver_setup):
    return LogoutPage(driver_setup)

@pytest.fixture(scope="module")
def login(driver_setup):
    login_page = LoginPage(driver_setup)
    login_page.open_login_page(Config.BASE_URL)
    return login_page

@pytest.fixture(scope="module")
def add_to_cart(driver_setup):
    return AddToCartPage(driver_setup)

@pytest.fixture(scope="module")
def payment(driver_setup):
    return PaymentPage(driver_setup)

@pytest.fixture(scope="module")
def logout(driver_setup):
    return LogoutPage(driver_setup)
