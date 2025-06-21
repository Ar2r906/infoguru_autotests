import pytest
from API.tests.tests_routes import tests_routes
from BASE.something import *
from API.tests.TestClass import BaseTests

@pytest.fixture(scope='session')
def create_delete_tests(get_access_token_admin, get_admin_uid):
    headers_data = {"x-access-token": f"{get_access_token_admin}"}
    tests = BaseTests(get_admin_uid)

    print("Request JSON:", tests.as_dict())  # для отладки
    print("Headers:", headers_data)

    response = post_something(
        tests_routes['create_tests']['url'],
        headers=headers_data,
        json=tests.as_dict()
    )

    assert response.status_code == 201
    created = response.json()["createdTest"]

    yield {
        "id": created["id"],
        "theme": created["theme"],
    }

    delete_response = delete_something(
        tests_routes['delete_tests']['url'].replace(":id", str(created["id"])),
        headers=headers_data,
    )
    assert delete_response.status_code in [200, 204, 404]