import pytest
import allure
from BASE.something import post_something
from auths_routes import auths_routes
from BASE.conftest import TestUser

negative_cases = [
    ("email", "invalid", 400),
    ("email", None, 400),
    ("email", "&*(", 400),
    ("email", "ibragimov_ar18@mail.ru", 409),

    ("f_name", 1, 400),
    ("f_name", None, 400),
    ("f_name", "%", 400),

    ("s_name", 110, 400),
    ("s_name", None, 400),
    ("s_name", "@", 400),

    ("p_name", 5, 400),
    ("p_name", None, 400),
    ("p_name", "&", 400),

    ("age", -1, 400),
    ("age", None, 400),
    ("age", "&", 400),

    ("user_class", -1, 400),
    ("user_class", None, 400),
    ("user_class", " ", 400),

    ("password", -1, 400),
    ("password", None, 400),
    ("password", " ", 400),
    ("password", "123456", 400),

    ("school", -1, 400),
    ("school", None, 400),
    ("school", " ", 400),
]

@pytest.mark.order(1)
class TestRegistrations:

    @allure.title("Negative registrations tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_registration(self, field, value, expected_status):
        # Создаем всегда новые данные (для чистоты теста)
        user = TestUser()
        data = user.copy_modified(field, value)

        response = post_something(auths_routes["signup"]["url"], json=data)
        assert response.status_code == expected_status