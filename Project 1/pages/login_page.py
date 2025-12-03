from pages.base_page import BasePage

class LoginPage(BasePage):
    def __init__(self, page):
        super().__init__(page)
        # Locators
        self.username = page.locator('[data-test="username"]')
        self.password = page.locator('[data-test="password"]')
        self.login_btn = page.locator('[data-test="login-button"]')

    def do_login(self, user, pwd):
        self.page.goto("https://www.saucedemo.com/")
        self.do_fill(self.username, user)
        self.do_fill(self.password, pwd)
        self.do_click(self.login_btn)