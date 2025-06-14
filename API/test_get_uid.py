import requests
import pytest
import os
from dotenv import load_dotenv
load_dotenv('../.env')

BASE_URL = os.getenv("DEV_URL_API")

@pytest.fixture
def valid_credentials():
    return {
        "email": "ibragimov_ar18@mail.ru",
        "password": "17r2d2#Builder@18",
    }

def test_get_uid(valid_credentials):
    response = requests.post(
        f"{BASE_URL}/auths/signin",
        json=valid_credentials,
    )

    response_data = response.json()
    access_token = response_data['AccessToken']
    uid = response_data['uid']

    assert response.status_code == 200
    assert response_data['email'] == valid_credentials['email']
    assert isinstance(response_data['uid'], str) and len(response_data['uid']) > 0
    assert isinstance(response_data['AccessToken'], str) and len(response_data['AccessToken']) > 0
    assert response_data['role'] in [1, 2, 3]

    return {
        'uid': uid,
        'access_token': access_token,
    }