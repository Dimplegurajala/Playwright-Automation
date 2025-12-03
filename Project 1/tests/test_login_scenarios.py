import pytest
from pages.login_page import LoginPage
from playwright.sync_api import expect

# DATA-DRIVEN TESTING (Standard vs Locked User)
@pytest.mark.parametrize("username, password, expected_url", [
    ("standard_user", "secret_sauce", "inventory.html"),
    ("locked_out_user", "secret_sauce", "https://www.saucedemo.com/"), 
])
def test_login_data_driven(page_context, username, password, expected_url):
    page = page_context
    login = LoginPage(page)

    login.do_login(username, password)

    # Assert URL based on user type
    expect(page).to_have_url(f"**/{expected_url}")