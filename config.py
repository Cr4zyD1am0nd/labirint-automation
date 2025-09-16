import os
from dotenv import load_dotenv

# Загружаем переменные окружения
load_dotenv()

BASE_URL = os.getenv("BASE_URL")
USER_EMAIL = os.getenv("USER_EMAIL")
