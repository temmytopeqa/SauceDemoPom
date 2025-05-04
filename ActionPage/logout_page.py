from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from LocatorPage.locator_page import LogoutLocators

class LogoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def open_menu(self):
        menu_button = self.wait.until(EC.element_to_be_clickable(LogoutLocators.MENU_BUTTON))
        menu_button.click()

    def click_logout(self):
        logout_link = self.wait.until(EC.element_to_be_clickable(LogoutLocators.LOGOUT_LINK))
        logout_link.click()

