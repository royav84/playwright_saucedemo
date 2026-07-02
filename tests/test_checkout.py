from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage


def test_successful_checkout_navigation(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)            
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    assert page.url == "https://www.saucedemo.com/checkout-step-two.html"

    
def test_checkout_error_missing_first_name(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)        
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")  
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.fill_first_name("")
    checkout_page.fill_last_name("Doe")     
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()  
    assert checkout_page.get_error_message() == "Error: First Name is required"


def test_checkout_error_missing_last_name(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")  
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.go_to_checkout()  
    checkout_page = CheckoutPage(page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == "Error: Last Name is required"

def test_checkout_error_missing_postal_code(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")  
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.go_to_checkout()  
    checkout_page = CheckoutPage(page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("")
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == "Error: Postal Code is required"

def test_click_finish_redirects_to_checkout_complete(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart() 
    cart_page = CartPage(page)  
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert page.url == "https://www.saucedemo.com/checkout-complete.html"

def test_checkout_complete_header_text(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(page)  
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert checkout_page.get_checkout_complete_header() == "Thank you for your order!"