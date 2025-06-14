from dotenv import load_dotenv
import os

load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

articles_routes = {
    'create_articles': {
        'url': f"{BASE_URL}/articles/create_articles",
        'method': 'POST',
        'expected_status': 201,
        'error_status': [400, 500],
    },
    'get_articles': {
        'url': f"{BASE_URL}/articles/get_articles",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [404, 500],
    },
    'get_articles_by_id': {
        'url': f"{BASE_URL}/articles/get_articles/{id}",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'edit_articles': {
        'url': f"{BASE_URL}/articles/edit_articles/{id}",
        'method': 'PATCH',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'delete_articles': {
        'url': f"{BASE_URL}/articles/delete_articles/{id}",
        'method': 'DELETE',
        'expected_status': 204,
        'error_status': [400, 404, 500],
    },
}
