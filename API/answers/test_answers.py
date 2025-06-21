import allure
import pytest
from API.auths.conftest import get_access_token_admin
from BASE.something import post_something, get_something
from API.answers.answers_routes import answers_routes

class TestAnswers:

    @allure.title('Negative create answers tests')
    @pytest.mark.parametrize("field, value, expected_status", [
        ('test_id', None, 400),
        ('question_id', None, 400),
        ('first_answer', None, 400),
        ('second_answer', None, 400),
        ('third_answer', None, 400),
        ('true_answer', None, 400),

        ('test_id', ' ', 400),
        ('question_id', ' ', 400),
        ('first_answer', ' ', 400),
        ('second_answer', ' ', 400),
        ('third_answer', ' ', 400),
        ('true_answer', ' ', 400),
    ])
    def test_negative_create_answers(self, field, value, expected_status, get_access_token_admin):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        data = {
            "test_id": 1,
            "question_id": 1,
            'first_answer': 1,
            'second_answer': 1,
            'third_answer': 1,
            'fourth_answer': 1,
            'true_answer': 1,
        }
        data[field] = value

        response = post_something(
            answers_routes['create_answers']['url'],
            headers=headers_data,
            json=data,
        )

        assert response.status_code == expected_status

    @allure.title('Negative get answer by id')
    @pytest.mark.parametrize("value, expected_status", [
        (10009, 404),
        (' ', 400),
        ('%', 400),
        ('string', 400)
    ])
    def test_negative_get_answer_by_id(self, value, expected_status, get_access_token_admin):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = get_something(
            answers_routes['get_answers_by_id']['url'].replace(':id', str(value)),
            headers=headers_data,
        )

        assert response.status_code == expected_status

    @allure.title('Negative get answer by test id')
    @pytest.mark.parametrize("value, expected_status", [
        (None, 400),
        (' ', 400),
        ('%', 400),
        ('string', 400)
    ])
    def test_negative_get_answer_by_test_id(self, value, expected_status, get_access_token_admin):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = get_something(
            answers_routes['get_answers_by_test_id']['url'].replace(':id', str(value)),
            headers=headers_data,
        )

        assert response.status_code == expected_status

    # @allure.title('Negative edit answer')
    # @pytest.mark.parametrize("value, expected_status", [])
    # def test_negative_edit_answer(self, value, expected_status, get_access_token_admin):
    #     return 0
    #
    # @allure.title('Negative delete answer')
    # @pytest.mark.parametrize("value, expected_status", [])
    # def test_negative_delete_answer(self, value, expected_status, get_access_token_admin):
    #     return 0