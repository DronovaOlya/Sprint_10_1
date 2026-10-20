import pytest
from selenium import webdriver
from page_object.pages.main_page import MainPage
from page_object.pages.main_page import MainPage


@pytest.fixture(scope="function")
def driver():
    browser = webdriver.Chrome()
    yield browser
    browser.quit()

@pytest.fixture
def main_page(driver):
    page = MainPage(driver)
    return page

