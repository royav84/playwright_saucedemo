class CheckoutPage:
    def __init__(self, page):
        self.page = page

    def fill_first_name(self, first_name):
        self.page.locator("[data-test='firstName']").fill(first_name)

    def fill_last_name(self, last_name):
        self.page.locator("[data-test='lastName']").fill(last_name)

    def fill_postal_code(self, postal_code):
        self.page.locator("[data-test='postalCode']").fill(postal_code)

    def click_continue(self):
        self.page.locator("[data-test='continue']").click()

    def get_error_message(self):
        return self.page.locator("[data-test='error']").inner_text()

    def click_finish(self):
        self.page.locator("[data-test='finish']").click()

    def get_checkout_complete_header(self):
        return self.page.locator("[data-test='complete-header']").inner_text()
    
    def get_subtotal(self):
        return self.page.locator("[data-test='subtotal-label']").inner_text()
    
    def get_tax(self):
        return self.page.locator("[data-test='tax-label']").inner_text()
    
    def get_total(self):
        return self.page.locator("[data-test='total-label']").inner_text()