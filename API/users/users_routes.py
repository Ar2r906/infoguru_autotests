from dotenv import load_dotenv
import os
load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

users_routes = {
    'get_email': {
        'url': f"{BASE_URL}/users/get_email",
        'method': 'GET',
        'expected_status': 200,
        'error': [400, 404, 500]
    },
    'get_info_about_user_by_uid': {
        'url': f"{BASE_URL}/users/get_info_about_user/:uid",
        'method': 'GET',
        'expected_status': 200,
        'error': [400, 404, 500]
    },
    'edit_users': {
        'url': f"{BASE_URL}/users/edit_users/:uid",
        'method': 'PATCH',
        'expected_status': 201,
        'error': [400, 404, 500]
    },
    'edit_role_users': {
        'url': f"{BASE_URL}/users/edit_role_by_email",
        'method': 'PATCH',
        'expected_status': 201,
        'error': [400, 403, 404, 500]
    },
    'delete_user': {
        'url': f"{BASE_URL}/users/delete_users",
        'method': 'DELETE',
        'expected_status': 204,
        'error': [400, 401, 403, 404, 500]
    }
}