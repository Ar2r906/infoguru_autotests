import allure
import pytest
from API.questions.questions_routes import questions_routes
from API.questions.conftest import create_delete_questions
from API.tests.conftest import create_delete_tests
from BASE.something import *
from API.questions.QuestionsClass import BaseQuestion
from API.auths.conftest import get_admin_uid, get_access_token_admin

class TestQuestions:

    @allure.title('Negative create questions tests')
    @pytest.mark.parametrize('field, value, expected_status', [
        ('test_id', " ", 400),
        ('test_id', None, 400),
        ('content', None, 400),
        ('content', ' ', 400)
    ])
    def test_create_negative(self, get_access_token_admin, field, value, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}
        json_data = {
            "test_id": "12",
            "content": "value"
        }
        json_data[field] = value

        response = post_something(
            questions_routes['create_questions']['url'],
            headers=headers_data,
            json=json_data,
        )

        assert response.status_code == expected_status

    @allure.title('Negative get questions by id tests')
    @pytest.mark.parametrize('value, expected_status', [
        (1000001, 404),
        ('string', 400),
        ("%", 400),
        (None, 400),
    ])
    def test_get_negative(self, get_access_token_admin, value, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = get_something(
            questions_routes['get_questions_by_id']['url'].replace(':id', str(value)),
            headers=headers_data,
        )

        assert response.status_code == expected_status

    @allure.title('Negative get questions by test_id')
    @pytest.mark.parametrize('value, expected_status', [
        (' ', 400),
        ('string', 400),
        ("%", 400),
        (None, 400),
    ])
    def test_get_by_test_id_negative(self, get_access_token_admin, value, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = get_something(
            questions_routes['get_questions_by_test_id']['url'].replace(':id', str(value)),
            headers=headers_data,
        )

        assert response.status_code == expected_status

    @allure.title('Negative edit questions tests')
    @pytest.mark.parametrize('field, value, expected_status', [
        ('test_id', " ", 404),
        ('test_id', None, 404),
        ('content', None, 404),
        ('content', ' ', 404),
        ('test_id', '%', 404),
    ])
    def test_edit_negative(self, get_access_token_admin, get_admin_uid, create_delete_tests, field, value, expected_status, create_delete_questions):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}
        questions_data = create_delete_questions
        questions_id = questions_data['id']
        json_data = {
            "test_id": "12",
            "content": "value"
        }
        json_data[field] = value

        response = patch_something(
            questions_routes['edit_question']['url'].replace(':id', str(questions_id)),
            headers=headers_data,
            json=json_data,
        )
        assert response.status_code == expected_status

    @allure.title('Negative delete questions tests')
    @pytest.mark.parametrize('value, expected_status', [
        (" ", 400),
        ("*", 400),
        ("str", 400),
        (111111111, 404),
    ])
    def test_delete(self, get_access_token_admin, value, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = delete_something(
            questions_routes['delete_question']['url'].replace(':id', str(value)),
            headers=headers_data,
        )

        assert response.status_code == expected_status