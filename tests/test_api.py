import pytest
import requests
from config import BASE_URL


@pytest.mark.api
def test_search_positive():
    """Позитивный поиск книги"""
    url = f"{BASE_URL}/search/Рим/?stype=0"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Рим" in response.text


@pytest.mark.api
def test_search_empty():
    """Поиск пустого запроса"""
    url = f"{BASE_URL}/search//?stype=0"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Ничего не найдено" in response.text


@pytest.mark.api
def test_search_special_chars():
    """Поиск со спецсимволами"""
    url = f"{BASE_URL}/search/!@#$%^&*()/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Ничего не найдено" in response.text


@pytest.mark.api
def test_search_nonexistent():
    """Поиск несуществующей книги"""
    url = f"{BASE_URL}/search/НетТакойКниги/"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Ничего не найдено" in response.text


@pytest.mark.api
def test_search_long_query():
    """Поиск очень длинной строки"""
    long_query = "а" * 500
    url = f"{BASE_URL}/search/{long_query}/"
    response = requests.get(url)
    assert response.status_code == 200
