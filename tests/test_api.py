# tests/test_api.py
import requests
import allure
from config import BASE_URL


@allure.feature("API: Поиск")
def test_search_positive() -> None:
    url = f"{BASE_URL}/search/Рим/?stype=0"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Рим" in response.text


@allure.feature("API: Поиск")
def test_search_empty() -> None:
    url = f"{BASE_URL}/search//?stype=0"
    response = requests.get(url)
    assert response.status_code == 200
    assert "Ничего не найдено" in response.text
