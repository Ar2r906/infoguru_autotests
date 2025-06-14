import pytest
from dotenv import load_dotenv
import os

CURRENT_DIR = os.path.dirname(os.path.abspath(__file__))
DOTENV_PATH = os.path.join(CURRENT_DIR, ".env")
load_dotenv(dotenv_path=DOTENV_PATH)

# Тест
print("BASE_URL =", os.getenv("DEV_URL_API"))

# Папка для результатов allure
ALLURE_RESULTS_DIR = os.path.join(CURRENT_DIR, "allure-results")
ALLURE_REPORT_DIR = os.path.join(CURRENT_DIR, "allure-report")

# Запуск тестов
exit_code = pytest.main([
    "API/auths",
    "-v",
    "--disable-warnings",
    f"--alluredir={ALLURE_RESULTS_DIR}"
])

if exit_code == 0:
    print(f"✅ Тесты прошли успешно, отчеты по тестам в allure-results")
else:
    print(f"❌ Тесты завершились с ошибками, exit code: {exit_code}")
