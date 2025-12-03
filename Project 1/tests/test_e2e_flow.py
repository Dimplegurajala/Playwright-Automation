from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_buy_product_end_to_end(page_context):
    page = page_context
    
    # 1. Initialize Pages
    login = LoginPage(page)
    products = ProductsPage(page)
    checkout = CheckoutPage(page)

    # 2. Login
    login.do_login("standard_user", "secret_sauce")
    expect(products.title).to_have_text("Products")

    # 3. Add to Cart (Retail Scenario)
    products.add_product_to_cart("Sauce Labs Backpack")
    expect(products.cart_badge).to_have_text("1")
    products.go_to_cart()

    # 4. Checkout Flow
    checkout.proceed_to_checkout()
    checkout.fill_shipping_info("Dimple", "Tester", "12345")
    checkout.complete_order()

    # 5. Verify Success
    expect(checkout.complete_header).to_have_text("Thank you for your order!")