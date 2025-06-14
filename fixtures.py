import pytest
from API.auths.auths_routes import auths_routes
from BASE.conftest import TestUser
from BASE.something import post_something

@pytest.fixture(scope="session")
def registered_user():
    user = TestUser()
    response = post_something(auths_routes['signup']['url'], json=user.as_dict())
    assert response.status_code == 201
    return user

@pytest.fixture(scope="session")
def access_token(registered_user):
    creds = {
        'email': registered_user.email,
        'password': registered_user.password,
    }

    response = post_something(auths_routes["signin"]["url"], json=creds)
    assert response.status_code == 200
    token = response.json().get["AccessToken"]
    assert token
    return token