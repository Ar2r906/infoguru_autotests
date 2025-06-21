from dotenv import load_dotenv
import os
load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

answers_routes = {
    'create_answers': {
        'url': f"{BASE_URL}/answers/create_answers",
        'method': 'POST',
        'expected_status': 201,
        'errors': [400, 500],
    },
    'get_answers': {
        'url': f"{BASE_URL}/answers/get_answers",
        'method': 'GET',
        'expected_status': 200,
        'errors': [404, 500],
    },
    'get_answers_by_id': {
        'url': f"{BASE_URL}/answers/get_answers/:id",
        'method': 'GET',
        'expected_status': 200,
        'errors': [400, 404, 500],
    },
    'get_answers_by_test_id': {
        'url': f"{BASE_URL}/answers/get_answers_by_test_id/:id",
        'method': 'GET',
        'expected_status': 200,
        'errors': [400, 404, 500],
    },
    'edit_answers': {
        'url': f"{BASE_URL}/answers/edit_answers/:id",
        'method': 'PATCH',
        'expected_status': 201,
        'errors': [400, 404, 500],
    },
    'delete_answer': {
        'url': f"{BASE_URL}/answers/delete_answers/:id",
        'method': 'DELETE',
        'expected_status': 204,
        'errors': [400, 404, 500],
    }
}