from selenium.webdriver.common.by import By

class LoginLocators:
    USERNAME = (By.ID, "user-name")
    PASSWORD = (By.ID, "password")
    LOGIN = (By.ID, "login-button")

class AddToCartLocators:
    BACKPACK = (By.ID, "add-to-cart-sauce-labs-backpack")
    BIKE_LIGHT = (By.ID, "add-to-cart-sauce-labs-bike-light")
    BOLT_T_SHIRT = (By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    FLEECE_JACKET = (By.ID, "add-to-cart-sauce-labs-fleece-jacket")
    ONESIE = (By.ID, "add-to-cart-sauce-labs-onesie")
    RED_T_SHIRT = (By.ID, "add-to-cart-test.allthethings()-t-shirt-(red)")
    CHECKOUT_BUTTON = (By.ID, "checkout")  # From the cart page

class GoToCartLocator:
    CART_ICON = (By.ID, "shopping_cart_container")

class LogoutLocators:
        MENU_BUTTON = (By.ID, "react-burger-menu-btn")
        LOGOUT_LINK = (By.ID, "logout_sidebar_link")