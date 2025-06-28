from Config.configuration import Config

def test_login_page_on_automation_play_ground_website(login):
    login.username(Config.USERNAME)
    login.password(Config.PASSWORD)
    login.click_button()

def test_add_to_cart_on_automation_play_ground_website(add_to_cart):
    add_to_cart.add_products_to_cart()
    add_to_cart.go_to_cart()
    add_to_cart.click_checkout()

def test_payment_page_on_automation_play_ground_website(payment):
    payment.complete_payment_process(
        first_name=Config.FIRST_NAME,
        last_name=Config.LAST_NAME,
        postal_code=Config.POSTAL_CODE
    )

def test_logout_page_on_automation_play_ground_website(logout):
    logout.open_menu()
    logout.click_logout()
