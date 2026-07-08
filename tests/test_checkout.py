from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.inventory_page import InventoryPage

def test_successful_checkout_navigation(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    assert logged_in_page.url == "https://www.saucedemo.com/checkout-step-two.html"

    
def test_checkout_error_missing_first_name(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("")
    checkout_page.fill_last_name("Doe")     
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()  
    assert checkout_page.get_error_message() == "Error: First Name is required"


def test_checkout_error_missing_last_name(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == "Error: Last Name is required"

def test_checkout_error_missing_postal_code(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("")
    checkout_page.click_continue()
    assert checkout_page.get_error_message() == "Error: Postal Code is required"

def test_click_finish_redirects_to_checkout_complete(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert logged_in_page.url == "https://www.saucedemo.com/checkout-complete.html"

def test_checkout_complete_header_text(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    checkout_page.click_finish()
    assert checkout_page.get_checkout_complete_header() == "Thank you for your order!"

def test_checkout_summary_calculations(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    inventory_page.click_add_to_cart_button("sauce-labs-bike-light")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.go_to_checkout()  
    checkout_page = CheckoutPage(logged_in_page)
    checkout_page.fill_first_name("John")
    checkout_page.fill_last_name("Doe")
    checkout_page.fill_postal_code("12345")
    checkout_page.click_continue()
    subtotal_text = checkout_page.get_subtotal()
    tax_text = checkout_page.get_tax()
    total_text = checkout_page.get_total()  
    subtotal = float(subtotal_text.split("$")[1])
    tax = float(tax_text.split("$")[1])
    total = float(total_text.split("$")[1])
    assert round(subtotal + tax, 2) == total