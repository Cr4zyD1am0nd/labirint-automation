# tests/test_ui.py
import pytest
from selenium import webdriver
from config import BASE_URL, USER_EMAIL
from pages.login_page import LoginPage


@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login_email(driver) -> None:
    """Тест: авторизация по email до экрана ввода кода"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)

    login_page.open_login()
    login_page.enter_email(USER_EMAIL)
    login_page.submit()

    assert "Код подтверждения" in driver.page_source
