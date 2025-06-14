from dotenv import load_dotenv
import os

load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

news_routes = {
    'create_news': {
        'url': f"{BASE_URL}/news/create_news",
        'method': 'POST',
        'expected_status': 201,
        'error_status': [400, 500],
    },
    'get_news': {
        'url': f"{BASE_URL}/news/get_news",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [404, 500],
    },
    'get_news_by_id': {
        'url': f"{BASE_URL}/news/get_news/{id}",
        'method': 'GET',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'edit_news': {
        'url': f"{BASE_URL}/news/edit_news/{id}",
        'method': 'PATCH',
        'expected_status': 200,
        'error_status': [400, 404, 500],
    },
    'delete_news': {
        'url': f"{BASE_URL}/news/delete_news/{id}",
        'method': 'DELETE',
        'expected_status': 204,
        'error_status': [400, 404, 500],
    },
}
