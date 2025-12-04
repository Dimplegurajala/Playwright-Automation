from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from playwright.sync_api import expect

def test_checkout_missing_info(page_context):
    """Negative Test: Verify form validation prevents progress."""
    page = page_context
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page) 
    checkout = CheckoutPage(page)
    
    login.do_login("standard_user", "secret_sauce")
    products.add_product_to_cart("Sauce Labs Backpack")
    products.go_to_cart()
    cart.proceed_to_checkout()
    
    # Click Continue WITHOUT filling shipping info
    checkout.click_continue_expecting_failure()
    
    # Assert Error Message
    assert "Error: First Name is required" in checkout.get_error_message()

def test_security_direct_url_access(page_context):
    """
    Security Test: Users cannot access internal pages without logging in.
    """
    page = page_context
    
    # 1. Try to go to Inventory WITHOUT logging in
    page.goto("https://www.saucedemo.com/inventory.html")
    
    # 2. Assert - without logging
    expect(page).not_to_have_url("https://www.saucedemo.com/inventory.html")
    expect(page.locator('[data-test="error"]')).to_contain_text("sadface: You can only access")