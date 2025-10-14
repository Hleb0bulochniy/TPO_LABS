from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.edge.options import Options
from pages.test_page import TestPage
from pages.contact_page import ContactPage
from pathlib import Path
import pytest


@pytest.fixture
def driver():
    driver_path = Path(__file__).resolve().parents[1] / "drivers" / "msedgedriver.exe"
    service = Service(executable_path=str(driver_path))
    opts = Options()
    drv = webdriver.Edge(service=service, options=opts)
    yield drv
    drv.quit()


def test_1(driver):
    page = TestPage(driver)
    page.open_page()
    page.fill_form("123", "Hello")
    page.submit()
    text = page.get_message()
    assert "Received" in text


def test_2(driver):
    page = TestPage(driver)
    page.open_page()
    page.fill_form("", "")
    page.submit()
    text = page.get_message()
    assert "Received" in text


def test_3(driver):
    page = ContactPage(driver)
    page.open_page()
    page.fill_form("123", "Hello world")
    page.submit()
    result = page.get_result()
    assert "Received" in result


def test_4(driver):
    page = ContactPage(driver)
    page.open_page()
    page.fill_form("123", "")
    page.submit()
    result = page.get_result()
    assert "Error" in result

def test_5(driver):
    page = ContactPage(driver)
    page.open_page()
    page.fill_form("", "123")
    page.submit()
    result = page.get_result()
    assert "Error" in result


def test_6(driver):
    page = ContactPage(driver)
    page.open_page()
    page.fill_form("", "")
    page.submit()
    result = page.get_result()
    assert "Error" in result
