import allure
import pytest
from BASE.something import *
from users_routes import users_routes
from DATA_GENERATOR import fakers
from API.auths.conftest import get_access_token_admin, created_auth_user

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

    #f_name, s_name, p_name, email, age, school, user_class
    @allure.title('Negative edit users tests')
    @pytest.mark.parametrize("field, value, expected_status", [
        ("age", -5, 201),
        ("user_class", "", 201),
        ("school", None, 201),
        ("f_name", 12345, 201),
    ])
    def test_negative_edit_users(self, field, value, expected_status, created_auth_user):
        uid = created_auth_user["uid"]
        headers_data = {"x-access-token": f"{created_auth_user["token"]}"}
        json_data = {
            field : value
        }
        response = patch_something(
            users_routes['edit_users']['url'].replace(":uid", str(uid)),
            headers=headers_data,
            json=json_data
        )
        assert response.status_code == expected_status

    @allure.title("Negative edit user role by email tests")
    @pytest.mark.parametrize("field, value, token_case, expected_status", [
        ("email", 1, "no_token", 403),
        ("email", None, "admin", 400),
        ("email", f"{fakers.generate_email}", "admin", 404),
        ("email", "ibragimov_ar18@mail.ru", "admin", 400),
    ])
    def test_negative_edit_user_role_by_email(self, field, value, token_case, get_access_token_admin, expected_status):
        if token_case == "no_token":
            headers_data = { }
        elif token_case == "admin":
            headers_data = { "x-access-token": f"{get_access_token_admin}"}
        else:
            raise ValueError("Unknown token_case")

        json_data = {
            field: value,
            "role_name": "user"
        }

        response = patch_something(
            users_routes["edit_role_users"]["url"],
            headers=headers_data,
            json=json_data
        )
        assert response.status_code == expected_status, \
        f"Expected {expected_status}, got {response.status_code}. Response: {response.text}"
        assert response.json()

    @allure.title("Negative delete user by email tests")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("email", "someone@example.com", 404),
        ("email", None, 400),
        ("email", "nonexistent@example.com", 404)
    ])
    def test_negative_delete_user_by_email(self, field, value, expected_status, get_access_token_admin):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}
        json_data = {
            field : value
        }

        response = delete_something(
            users_routes['delete_user']['url'],
            headers=headers_data,
            json=json_data
        )

        assert response.status_code == expected_status