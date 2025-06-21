import pytest
import allure
from BASE.something import *
from API.tests import TestClass
from tests_routes import tests_routes
from conftest import *
from API.auths.conftest import get_access_token_admin, get_admin_uid

class TestTests:

    @allure.title("Negative create test")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("theme", None, 400),
        ("theme", 1, 400),
        ("theme", " ", 400),
    ])
    def test_create_negative(self, field, value, get_admin_uid, get_access_token_admin, expected_status):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}
        json_data = {
            field: value,
            "uid": get_admin_uid,
        }

        response = post_something(
            tests_routes['create_tests']['url'],
            headers=headers_data,
            json=json_data,
        )
        assert response.status_code == expected_status

    @allure.title("Negative edit test")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("theme", None, 400),
        ("theme", 1234, 400),
        ("theme", " ", 400),
    ])
    def test_edit_negative(self, field, value, get_admin_uid, create_delete_tests, get_access_token_admin, expected_status):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}
        tests_id = create_delete_tests["id"]

        tests_data_theme = BaseTests(get_admin_uid).as_dict()

        tests_data_theme[field] = value

        response = patch_something(
            tests_routes['edit_tests']['url'].replace(':id', str(tests_id)),
            headers=headers_data,
            json=tests_data_theme,
        )

        assert response.status_code == expected_status

    @allure.title("Negative get test")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("id", None, 400),
        ("id", 12345, 404),
        ("id", "string", 400)
    ])
    def test_get_negative(self, field, value, get_access_token_admin, expected_status):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}

        response = get_something(
            tests_routes['get_tests_by_id']['url'].replace(f':{field}', str(value)),
            headers=headers_data
        )

        assert response.status_code == expected_status

    @allure.title("Negative delete test")
    @pytest.mark.parametrize("field, value, expected_status", [
        ("id", None, 400),
        ("id", 12345, 404),
        ("id", "string", 400)
    ])
    def test_delete_none(self, field, value, get_access_token_admin, expected_status):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}

        response = delete_something(
            tests_routes['delete_tests']['url'].replace(f':{field}', str(value)),
            headers=headers_data
        )

        assert response.status_code == expected_status