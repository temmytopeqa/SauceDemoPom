from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from LocatorPage.payment_locators import PaymentLocators

class PaymentPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 20)

    def enter_first_name(self, first_name):
        self.wait.until(EC.presence_of_element_located(PaymentLocators.FIRST_NAME)).send_keys(first_name)

    def enter_last_name(self, last_name):
        self.wait.until(EC.presence_of_element_located(PaymentLocators.LAST_NAME)).send_keys(last_name)

    def enter_postal_code(self, postal_code):
        self.wait.until(EC.presence_of_element_located(PaymentLocators.POSTAL_CODE)).send_keys(postal_code)

    def click_continue(self):
        self.wait.until(EC.element_to_be_clickable(PaymentLocators.CONTINUE_BUTTON)).click()

    def click_finish(self):
        self.wait.until(EC.element_to_be_clickable(PaymentLocators.FINISH_BUTTON)).click()

    def complete_payment_process(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        self.click_continue()
        self.click_finish()
