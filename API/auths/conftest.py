import pytest
import os
from API.auths.AuthClass import BaseUser
from BASE.something import *
from API.auths.auths_routes import auths_routes
from API.users.users_routes import users_routes
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

@pytest.fixture(scope="session")
def created_auth_user(get_access_token_admin):
    user = BaseUser()
    json_data = user.as_dict()

    response_register = post_something(
        auths_routes['signup']['url'],
        json=json_data
    )
    assert response_register.status_code == 201

    signin_response = post_something(
        auths_routes['signin']['url'],
        json={"email": user.email, "password": user.password}
    )
    assert signin_response.status_code == 200

    token = signin_response.json()['AccessToken']
    uid = signin_response.json()['uid']

    yield {
        'email': user.email,
        'uid': uid,
        'token': token,
        'password': user.password,
        'f_name': user.f_name,
        's_name': user.s_name,
        'p_name': user.p_name,
        'age': user.age,
    }

    delete_response = delete_something(
        users_routes['delete_user']['url'],
        headers={"x-access-token": f"{get_access_token_admin}"},
        json={"email": user.email}
    )
    assert delete_response.status_code in [200, 204]

@pytest.fixture(scope="session")
def get_admin_uid():
    creds = {
        'email': f'{EMAIL_ADMIN}',
        'password': f'{PASS_ADMIN}',
    }
    response = post_something(auths_routes['signin']['url'], json=creds)
    assert response.status_code == 200
    uid = response.json().get('uid')
    assert uid
    return uid