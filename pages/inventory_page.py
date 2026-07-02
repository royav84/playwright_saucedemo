class InventoryPage:

    def __init__(self, page):
        self.page = page

    def navigate(self):
        self.page.goto("https://www.saucedemo.com/inventory.html")

    def get_title(self):
        return self.page.locator("[data-test='title']").inner_text()

    def get_product_count(self):
        return self.page.locator("[data-test='inventory-item']").count()
    
    def is_dropdown_filter_visible(self):
        return self.page.locator("[data-test='product-sort-container']").is_visible()
    
    def click_add_to_cart_button(self, product_name):
        self.page.locator(f"[data-test='add-to-cart-{product_name}']").click()

    def get_cart_count(self):
        return self.page.locator("[data-test='shopping-cart-badge']").inner_text()   
    
    def get_product_list(self):
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()
    
    def select_filter_option(self, option_text):
        self.page.select_option("[data-test='product-sort-container']", label=option_text)

    def go_to_cart(self):
        self.page.locator("[data-test='shopping-cart-link']").click()
        