from selenium.webdriver.common.by import By
from .base_page import BasePage
from pathlib import Path

class ContactPage(BasePage):
    URL = (Path(__file__).resolve().parents[1] / "site" / "contact.html").as_uri()

    NAME = (By.ID, "name")
    MSG = (By.ID, "msg")
    BTN = (By.ID, "send")
    OK = (By.ID, "ok")
    ERR = (By.ID, "error")

    def open_page(self):
        self.open(self.URL)

    def fill_form(self, name, msg):
        self.type(self.NAME, name)
        self.type(self.MSG, msg)

    def submit(self):
        self.click(self.BTN)

    def get_result(self):
        try:
            ok_text = self.get_text(self.OK)
        except Exception:
            ok_text = ""
        try:
            err_text = self.get_text(self.ERR)
        except Exception:
            err_text = ""
        return ok_text or err_text
