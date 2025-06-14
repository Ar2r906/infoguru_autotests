from dotenv import load_dotenv
import os
load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

tests_routes = {
    'get_all_tests': {
        'url': f"{BASE_URL}/tests/get_tests_all",
        'method': 'GET',
        'expected_status': 200,
        'error': [404, 500]
    },
    'get_tests_by_id': {
        'url': f"{BASE_URL}/tests/get_tests/{id}",
        'method': 'GET',
        'expected_status': 200,
        'error': [400, 404, 500]
    },
    'create_tests': {
        'url': f"{BASE_URL}/tests/create_tests",
        'method': 'POST',
        'expected_status': 201,
        'error': [400, 500]
    },
    'edit_tests': {
        'url': f"{BASE_URL}/tests/edit_tests/{id}",
        'method': 'PATCH',
        'expected_status': 201,
        'error': [400, 404, 500]
    },
    'delete_tests': {
        'url': f"{BASE_URL}/tests/delete_tests/{id}",
        'method': 'DELETE',
        'expected_status': 204,
        'error': [400, 404, 500]
    }
}