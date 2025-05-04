from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from LocatorPage.locator_page import AddToCartLocators, GoToCartLocator

class AddToCartPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    # Add products to the cart
    def add_products_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.BACKPACK)).click()
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.BIKE_LIGHT)).click()
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.BOLT_T_SHIRT)).click()
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.FLEECE_JACKET)).click()
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.ONESIE)).click()
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.RED_T_SHIRT)).click()

    # Navigate to the shopping cart
    def go_to_cart(self):
        self.wait.until(EC.element_to_be_clickable(GoToCartLocator.CART_ICON)).click()

    # Click the checkout button to proceed
    def click_checkout(self):
        self.wait.until(EC.element_to_be_clickable(AddToCartLocators.CHECKOUT_BUTTON)).click()
