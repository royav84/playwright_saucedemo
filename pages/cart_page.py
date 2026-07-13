class CartPage:

    def __init__(self, page):
        self.page = page

    def go_to_checkout(self):
        self.page.locator("[data-test='checkout']").click()

    def continue_shopping(self):
        self.page.locator("[data-test='continue-shopping']").click()

    def get_cart_items(self):
        return self.page.locator("[data-test='inventory-item']").count()
    
    def get_item_names(self):
        return self.page.locator("[data-test='inventory-item-name']").all_inner_texts()
    
    def remove_item(self, product_name):
        self.page.locator(f"[data-test='remove-{product_name}']").click()


