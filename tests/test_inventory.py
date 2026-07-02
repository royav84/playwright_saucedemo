from pages.inventory_page import InventoryPage
from pages.login_page import LoginPage

def test_inventory_page_title(page):

    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    assert inventory_page.get_title() == "Products"

def test_inventory_page_product_count(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)    
    assert inventory_page.get_product_count() == 6

def test_inventory_page_has_visible_dropdown_filter(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    assert inventory_page.is_dropdown_filter_visible() == True

def test_add_to_cart_increments_cart_badge(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.click_add_to_cart_button("sauce-labs-backpack")
    assert inventory_page.get_cart_count() == "1"

def test_product_list_order_is_a_to_z_after_filter(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)               
    product_list = inventory_page.get_product_list()
    assert product_list == sorted(product_list)

def test_product_list_order_is_z_to_a_after_filter(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.select_filter_option("Name (Z to A)")
    product_list = inventory_page.get_product_list()
    assert product_list == sorted(product_list, reverse=True)

def test_add_all_items_to_cart_updates_badge_to_six(page):
    login_page = LoginPage(page)
    login_page.navigate()
    login_page.login("standard_user", "secret_sauce")
    inventory_page = InventoryPage(page)
    inventory_page.add_all_items_to_cart()
    assert inventory_page.get_cart_count() == "6"
