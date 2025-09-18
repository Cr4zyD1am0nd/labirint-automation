import pytest
from config import BASE_URL, USER_EMAIL
from pages.login_page import LoginPage


@pytest.mark.ui
def test_login_email(driver):
    """Тест: авторизация по email до экрана ввода кода"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.enter_email(USER_EMAIL)
    login_page.submit()
    assert "Код подтверждения" in driver.page_source


@pytest.mark.ui
def test_login_invalid_email(driver):
    """Тест: неверный email"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.enter_email("invalid@example.com")
    login_page.submit()
    assert "Неверный email" in driver.page_source


@pytest.mark.ui
def test_login_empty_email(driver):
    """Тест: пустое поле email"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.enter_email("")
    login_page.submit()
    assert "Поле email не может быть пустым" in driver.page_source


@pytest.mark.ui
def test_login_nonexistent_email(driver):
    """Тест: несуществующий email"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.enter_email("noone@example.com")
    login_page.submit()
    assert "Пользователь не найден" in driver.page_source


@pytest.mark.ui
def test_login_cancel(driver):
    """Тест: отмена авторизации"""
    driver.get(BASE_URL)
    login_page = LoginPage(driver)
    login_page.open_login()
    login_page.cancel()
    assert driver.current_url == BASE_URL
