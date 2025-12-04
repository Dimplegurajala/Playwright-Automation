from pages.base_page import BasePage

class ProductsPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        self.title = page.locator(".title")
        self.cart_badge = page.locator(".shopping_cart_badge")
        self.cart_link = page.locator(".shopping_cart_link")
        self.sort_dropdown = page.locator(".product_sort_container")
        self.price_elements = page.locator(".inventory_item_price")
        
        # Sidebar for Logout
        self.burger_menu = page.locator("#react-burger-menu-btn")
        self.logout_link = page.locator("#logout_sidebar_link")

    def add_product_to_cart(self, product_name):
        product_btn = self.page.locator(f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']//button")
        self.do_click(product_btn)

    def go_to_cart(self):
        self.do_click(self.cart_link)

    # --- NEW SDET II METHODS ---
    def select_sort_option(self, option_value):
        # Options: 'az', 'za', 'lohi', 'hilo'
        self.sort_dropdown.select_option(option_value)

    def get_all_price_values(self):
        # 1. Scrape all price texts (e.g., ["$29.99", "$9.99"])
        price_texts = self.price_elements.all_text_contents()
        
        # 2. Python List Comprehension: Clean '$' and convert to float
        return [float(p.replace("$", "")) for p in price_texts]

    def do_logout(self):
        self.do_click(self.burger_menu)
        self.do_click(self.logout_link)