# flake8: noqa: E402
import sys
import os
import pytest

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))

from selenium import webdriver


@pytest.fixture
def driver():
    """Фикстура для запуска и завершения браузера"""
    driver = webdriver.Chrome()
    driver.maximize_window()
    yield driver
    driver.quit()
