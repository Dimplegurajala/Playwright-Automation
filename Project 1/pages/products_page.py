from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")

    def add_product_to_cart(self, product_name):
        # Finds the specific button for the product
        product_btn = self.page.locator(f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.do_click(product_btn)

    def go_to_cart(self):
        self.do_click(self.cart_link)