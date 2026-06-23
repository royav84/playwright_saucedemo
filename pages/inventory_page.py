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