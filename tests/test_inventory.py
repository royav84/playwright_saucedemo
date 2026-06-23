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