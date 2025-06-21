import pytest
import allure
from BASE.something import post_something
from auths_routes import auths_routes
from API.auths.conftest import registered_user
import os
from dotenv import load_dotenv

load_dotenv('../../.env')
EMAIL_ADMIN = os.getenv('MAIN_EMAIL')
PASS_ADMIN = os.getenv('MAIN_PASS')

negative_cases = [
    ("email", "invalid", 400),
    ("email", None, 400),
    ("email", "&*(", 400),
    ("email", "ibragimov_ar18@mail.ru", 200),
    ("email", "noneemail@example.com", 404),

    ("password", "123456", 400),
    ("password", None, 400),
    ("password", "&*(", 400),
    ("password", "", 400),
]

@pytest.mark.order(2)
class TestAuths:

    @allure.title("Negative auths tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_auth(self, field, value, expected_status):
        auth_data = {
            'email': EMAIL_ADMIN,
            'password': PASS_ADMIN,
        }
        auth_data[field] = value

        response = post_something(auths_routes["signin"]["url"], json=auth_data)
        assert response.status_code == expected_status