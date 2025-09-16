# tests/conftest.py
import sys
import os

# Добавляем корень проекта для импорта config.py
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), "..")))
