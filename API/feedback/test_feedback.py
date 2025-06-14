import pytest
import allure
from BASE.something import post_something
from feedback_routes import feedback_routes

negative_cases = [
    ("email", None, 400),
    ("name", None, 400),
    ("message", None, 400),
]

class TestFeedback:

    @allure.title('Negative feedback tests')
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_feedback(self, field, value, expected_status):
        feedback_data = {
            "name": "Valid Name",
            "email": "validemail@example.com",
            "message": "Valid message",
        }
        feedback_data[field] = value

        response = post_something(feedback_routes["create_feedback"]["url"], json=feedback_data)
        assert response.status_code == expected_status

    @allure.title('Positive feedback tests')
    def test_positive_feedback(self):
        feedback_data = {
            'name': 'Artur',
            'email': 'ibragimov_ar18@mail.ru',
            'message': 'Test message',
        }
        response = post_something(feedback_routes["create_feedback"]["url"], json=feedback_data)
        assert response.status_code == 200