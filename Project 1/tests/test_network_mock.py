from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_simulate_image_failure(page_context):
    page = page_context
    
    # NETWORK MOCKING: Block all images to simulate CDN crash
    page.route("**/*.jpg", lambda route: route.abort())

    login = LoginPage(page)
    login.do_login("standard_user", "secret_sauce")

    # Assert page loads even if images are broken (Resilience)
    expect(page.locator(".title")).to_have_text("Products")