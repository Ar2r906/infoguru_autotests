import allure
import pytest
from BASE.something import *
from users_routes import users_routes
from DATA_GENERATOR import fakers
from API.auths.conftest import get_access_token_admin

class TestUsers:

    @allure.title("Negative get email tests")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("email", 1, 500),
        ("email", None, 404),
        ("email", "y@not", 404),
        ("email", f"{fakers.generate_email}", 404),
        ("email", f"{fakers.generate_email}", 404)
    ])
    def test_negative_get_email(self, field, value, expected_status, get_access_token_admin):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}

        data = { "email": 'email' }
        data[field] = value

        response = get_something(users_routes['get_email']['url'],headers=headers_data,json=data)

        assert response.status_code == expected_status
        assert response.json()

    @allure.title("Negative get info about user uid tests")
    @pytest.mark.parametrize("value, expected_status", [
        (1, 500),
        (fakers.generate_number, 500),
        ("edcbnlm-2decd", 500),
        ("466735ef-f669-45bb-8a38-3eca3c63bce9", 200)
    ])
    def test_negative_get_info(self, value, expected_status, get_access_token_admin):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}

        response = get_something(users_routes['get_info_about_user_by_uid']['url'].replace(":uid", str(value)),headers=headers_data)

        assert response.status_code == expected_status
        assert response.json()

