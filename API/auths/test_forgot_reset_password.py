import pytest
import allure
from BASE.something import post_something
from auths_routes import auths_routes
from fixtures import registered_user

@pytest.fixture(scope="session")
def reset_token(registered_user):
    response = post_something(
        auths_routes["forgot-password"]["url"],
        json={"email": registered_user.email}
    )
    assert response.status_code == 200
    token = response.json().get("token")
    assert token is not None
    return token

@pytest.mark.order(3)
class TestPasswordReset:

    @allure.title('Negative forgot password tests')
    @pytest.mark.parametrize("email, expected_status", [
        (" ", 400),
        ("invalid-email", 400),
        (None, 400),
        ("not-registered@example.com", 404)
    ])
    def test_password_forgot_negative(self, email, expected_status):
        response = post_something(
            auths_routes["forgot-password"]["url"],
            json={"email": email}
        )
        assert response.status_code == expected_status

    @allure.title('Negative reset password tests')
    @pytest.mark.parametrize("token, new_pass, expected_status", [
        ("", "ValidPass123!", 400),
        ("invalidtoken", "ValidPass123!", 400),
        (None, "ValidPass123!", 400),
        ("validtoken", "", 400),
        ("validtoken", None, 400),
        ("validtoken", "123", 400),
    ])
    def test_password_reset_negative(self, token, new_pass, expected_status, reset_token):
        # Если передан "validtoken", подменяем его реальным из фикстуры
        token_to_use = reset_token if token == "validtoken" else token

        response = post_something(
            auths_routes["reset-password"]["url"],
            json={
                "token": token_to_use,
                "new_pass": new_pass
            }
        )
        assert response.status_code == expected_status

    @allure.title('Positive reset password tests')
    def test_password_reset_positive(self, reset_token):
        response = post_something(
            auths_routes["reset-password"]["url"],
            json={
                "token": reset_token,
                "new_pass": "18r2d2#AlexyB&*"
            }
        )
        assert response.status_code == 201