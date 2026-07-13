from pages.cart_page import CartPage
from pages.inventory_page import InventoryPage

def test_item_added_with_correct_name(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-bike-light")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    names = cart_page.get_item_names()
    assert "Sauce Labs Bike Light" in names

def test_remove_item_from_cart_to_be_empty(logged_in_page):
    inventory_page = InventoryPage(logged_in_page)
    inventory_page.click_add_to_cart_button("sauce-labs-bike-light")
    inventory_page.go_to_cart()
    cart_page = CartPage(logged_in_page)
    cart_page.remove_item("sauce-labs-bike-light")
    listOFItems = cart_page.get_cart_items()
    assert listOFItems == 0

