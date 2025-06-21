from datetime import datetime

import pytest
from dotenv import load_dotenv
import os
import datetime
CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(CURRENT_DIR, ".env")
load_dotenv(dotenv_path=DOTENV_PATH)

# Тест
print("BASE_URL =", os.getenv("DEV_URL_API"))
print('Время начала: ', datetime.datetime.now())

# Папка для результатов allure
ALLURE_RESULTS_DIR = os.path.join(CURRENT_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(CURRENT_DIR, "allure-report")

# Запуск тестов
exit_code = pytest.main([
    "API/auths",
    "API/news",
    "API/articles",
    "API/feedback",
    "API/tests",
    "API/users",
    "API/questions",
    "-v", # режим verbose (подробный вывод: test_login.py::TestAuth::test_success PASSED)
    # "--disable-warnings",
    #f"--alluredir={ALLURE_RESULTS_DIR}"
])

if exit_code == 0:
    print(f"✅ Тесты прошли успешно, отчеты по тестам в allure-results")
    print('Время завершения: ', datetime.datetime.now())
else:
    print(f"❌ Тесты завершились с ошибками, exit code: {exit_code}")
