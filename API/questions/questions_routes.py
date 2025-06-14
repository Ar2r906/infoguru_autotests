from dotenv import load_dotenv
import os
load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

questions_routes = {
    'create_questions': {
        'url': f"{BASE_URL}/questions/create_questions",
        'method': 'POST',
        'expected_status': 201,
        'error_status': [400, 500],
    },
    'get_questions': {
        'url': f"{BASE_URL}/questions/get_questions",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [404, 500],
    },
    'get_questions_by_id': {
        'url': f"{BASE_URL}/questions/get_questions/{id}",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'get_questions_by_test_id': {
        'url': f"{BASE_URL}/questions/get_questions_by_id_tests/{id}",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'edit_question': {
        'url': f"{BASE_URL}/questions/edit_question/{id}",
        'method': 'PATCH',
        'expected_status': 201,
        'error_status': [400, 404, 500],
    },
    'delete_question': {
        'url': f"{BASE_URL}/questions/delete_questions/{id}",
        'method': 'DELETE',
        'expected_status': 204,
        'error_status': [400, 404, 500],
    }
}