from pages.base_page import BasePage

class CartPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.cart_item = page.locator(".cart_item")
        self.checkout_btn = page.locator('[data-test="checkout"]')
        self.remove_buttons = page.locator("button[id^='remove-']") # Starts with 'remove-'

    def get_cart_item_count(self):
        return self.cart_item.count()

    def remove_first_item(self):
        # Removes the top item in the list
        self.remove_buttons.first.click()

    def proceed_to_checkout(self):
        self.do_click(self.checkout_btn)