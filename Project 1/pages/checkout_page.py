from pages.base_page import BasePage

class CheckoutPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.first_name = page.locator('[data-test="firstName"]')
        self.last_name = page.locator('[data-test="lastName"]')
        self.zip_code = page.locator('[data-test="postalCode"]')
        self.continue_btn = page.locator('[data-test="continue"]')
        self.finish_btn = page.locator('[data-test="finish"]')
        self.complete_header = page.locator(".complete-header")

    def proceed_to_checkout(self):
        self.do_click(self.checkout_btn)

    def fill_shipping_info(self, fname, lname, zip):
        self.do_fill(self.first_name, fname)
        self.do_fill(self.last_name, lname)
        self.do_fill(self.zip_code, zip)
        self.do_click(self.continue_btn)

    def complete_order(self):
        self.do_click(self.finish_btn)