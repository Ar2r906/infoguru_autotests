import os
from dotenv import load_dotenv
load_dotenv('../../.env')

BASE_URL = os.getenv('DEV_URL_API')

auths_routes = {
    'signup': {
        'url': f"{BASE_URL}/auths/signup",
        'method': 'POST',
        'expected_status': 201,
        'error_status': [400, 409, 500],
    },
    'signin': {
        'url': f"{BASE_URL}/auths/signin",
        'method': 'POST',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'change-access': {
        'url': f"{BASE_URL}/auths/change-access",
        'method': 'POST',
        'expected_status': 200,
        'error_status': [404, 500],
    },
    'forgot-password': {
        'url': f"{BASE_URL}/auths/forgot-password",
        'method': 'POST',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'reset-password': {
        'url': f"{BASE_URL}/auths/reset-password",
        'method': 'POST',
        'expected_status': 201,
        'error_status': [400, 404, 500],
    }
}
