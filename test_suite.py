import pytest
from selenium import webdriver
from ActionPage.login_page import LoginPage
from ActionPage.add_to_cart import AddToCartPage
from ActionPage.logout_page import LogoutPage
from ActionPage.payment_page import PaymentPage
from selenium.webdriver.chrome.options import Options
from Config.configuration import Config

@pytest.fixture(scope="module")
def driver_setup():
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # Run Chrome in headless mode
    chrome_options.add_argument("--disable-gpu")  # Disable GPU acceleration (to avoid errors in headless mode)
    driver = webdriver.Chrome(options=chrome_options)
    driver.implicitly_wait(30)
    driver.maximize_window()
    yield driver
    driver.quit()

@pytest.fixture(scope="module")
def login(driver_setup):
    driver = driver_setup
    login_page = LoginPage(driver)
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


def test_login_page_on_automation_play_ground_website(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.click_button()

def test_add_to_cart_on_automation_play_ground_website(add_to_cart):
    add_to_cart.add_products_to_cart()
    add_to_cart.go_to_cart()
    add_to_cart.click_checkout()  # Moved here

def test_payment_page_on_automation_play_ground_website(payment):
    payment.complete_payment_process(
        first_name=Config.FIRST_NAME,
        last_name=Config.LAST_NAME,
        postal_code=Config.POSTAL_CODE
    )
def test_logout_page_on_automation_play_ground_website(logout):
    logout.open_menu()
    logout.click_logout()