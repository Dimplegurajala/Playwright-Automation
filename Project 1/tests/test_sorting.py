from pages.login_page import LoginPage
from pages.products_page import ProductsPage

def test_price_high_to_low(page_context):
    """
    Scraping data from UI - converting types, 
    and verifiying the sorting algorithm using Python logic.
    """
    page = page_context
    login = LoginPage(page)
    products = ProductsPage(page)

    login.do_login("standard_user", "secret_sauce")
    
    # 1. Select 'Price (high to low)'
    products.select_sort_option("hilo")
    
    # 2. Scrape the prices (Returns [49.99, 29.99, ...])
    actual_prices = products.get_all_price_values()
    
    # 3. Verify Logic
    # We sort the list manually in Python to see what it SHOULD look like
    expected_prices = sorted(actual_prices, reverse=True)
    
    print(f"UI Prices: {actual_prices}")
    
    assert actual_prices == expected_prices, "Prices are not sorted High to Low!"