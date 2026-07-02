class CartPage:

    def __init__(self, page):
        self.page = page

    def go_to_checkout(self):
        self.page.locator("[data-test='checkout']").click()

    def continue_shopping(self):
        self.page.locator("[data-test='continue-shopping']").click()

    def get_cart_items(self):
        return self.page.locator("[data-test='inventory-item']").count()