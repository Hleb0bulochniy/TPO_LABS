from selenium.webdriver.common.by import By
from .base_page import BasePage

class TestPage(BasePage):
    URL = "https://www.selenium.dev/selenium/web/web-form.html"

    TEXT_FIELD = (By.NAME, "my-text")
    TEXTAREA = (By.NAME, "my-textarea")
    BUTTON = (By.CSS_SELECTOR, "button")
    MESSAGE = (By.ID, "message")

    def open_page(self):
        self.open(self.URL)

    def fill_form(self, text1, text2):
        self.type(self.TEXT_FIELD, text1)
        self.type(self.TEXTAREA, text2)

    def submit(self):
        self.click(self.BUTTON)

    def get_message(self):
        return self.get_text(self.MESSAGE)
