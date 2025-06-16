import pytest
import os
from API.auths.AuthClass import BaseUser
from BASE.something import *
from API.auths.auths_routes import auths_routes
from dotenv import load_dotenv

load_dotenv('../../.env')
EMAIL_ADMIN = os.getenv('MAIN_EMAIL')
PASS_ADMIN = os.getenv('MAIN_PASS')

# регистрация пользователя, по сути это и есть позитивный тест-кейс
@pytest.fixture(scope="session")
def registered_user():
    user = BaseUser()
    response = post_something(auths_routes['signup']['url'], json=user.as_dict())
    assert response.status_code == 201
    return user

# авторизация обычного пользователя // получение токена пользователя
@pytest.fixture(scope="session")
def access_token(registered_user):
    creds = {
        'email': registered_user.email,
        'password': registered_user.password,
    }
    response = post_something(auths_routes["signin"]["url"], json=creds)
    assert response.status_code == 200
    token = response.json().get("AccessToken")
    assert token
    return token

# авторизация админа // получение токена админа
@pytest.fixture(scope="session")
def get_access_token_admin():
    creds = {
        'email': f'{EMAIL_ADMIN}',
        'password': f'{PASS_ADMIN}',
    }
    response = post_something(auths_routes['signin']['url'], json=creds)
    assert response.status_code == 200
    token = response.json().get('AccessToken')
    assert token
    return token
