class BasePage:
    def __init__(self, page):
        self.page = page

    # WRAPPER METHODS (Safe Actions)
    def do_click(self, locator):
        locator.wait_for(state="visible")
        locator.click()

    def do_fill(self, locator, text):
        locator.wait_for(state="visible")
        locator.fill(text)
        
    def get_text(self, locator):
        locator.wait_for(state="visible")
        return locator.text_content()