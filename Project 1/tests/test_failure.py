from pages.login_page import LoginPage
from playwright.sync_api import expect

def test_intentional_failure(page_context):
    page = page_context
    login = LoginPage(page)

    # 1. Login successfully
    login.do_login("standard_user", "secret_sauce")

    # 2. INTENTIONAL BUG: Assert the wrong title
    # The real title is "Swag Labs", but we expect "Amazon"
    print("\n⚠️ Intentional failure starting now...")
    expect(page).to_have_title("Appukutti")