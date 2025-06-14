from dotenv import load_dotenv
import os

load_dotenv('../../.env')
BASE_URL = os.getenv("DEV_URL_API")

feedback_routes = {
    'create_feedback': {
        'url': f"{BASE_URL}/feedback/create_feedback",
        'method': 'POST',
        'expected_status': 200,
        'error_status': [400, 500],
    }
}
