from pages.login_page import LoginPage
from pages.products_page import ProductsPage
from pages.cart_page import CartPage
from playwright.sync_api import expect

def test_cart_persistence_after_logout(page_context):
    """
    SDET II Scenario: Verifies that cart data is saved on the server/local storage
    even after the user logs out and logs back in.
    """
    page = page_context
    login = LoginPage(page)
    products = ProductsPage(page)
    
    # 1. Login and Add Item
    login.do_login("standard_user", "secret_sauce")
    products.add_product_to_cart("Sauce Labs Backpack")
    
    # 2. LOGOUT
    products.do_logout()
    
    # 3. LOGIN AGAIN
    # (Notice we don't navigate, we are already at login screen)
    login.do_fill(login.username, "standard_user")
    login.do_fill(login.password, "secret_sauce")
    login.do_click(login.login_btn)
    
    # 4. ASSERT: Item is STILL in the cart
    expect(products.cart_badge).to_have_text("1")

def test_cart_remove_item(page_context):
    """
    Verifies DOM reactivity: Removing an item should instantly update the badge.
    """
    page = page_context
    login = LoginPage(page)
    products = ProductsPage(page)
    cart = CartPage(page)
    
    login.do_login("standard_user", "secret_sauce")
    
    # Add 2 items
    products.add_product_to_cart("Sauce Labs Backpack")
    products.add_product_to_cart("Sauce Labs Bike Light")
    expect(products.cart_badge).to_have_text("2")
    
    # Go to cart and remove one
    products.go_to_cart()
    cart.remove_first_item()
    
    # Assert badge dropped to 1
    expect(products.cart_badge).to_have_text("1")