import pytest
from BASE.something import *
from API.auths.conftest import *
from API.tests.conftest import create_delete_tests
from API.questions.questions_routes import questions_routes

@pytest.fixture(scope="session")
def create_delete_questions(get_admin_uid, get_access_token_admin, create_delete_tests):
    test = create_delete_tests
    headers_data = {'x-access-token': f'{get_access_token_admin}'}

    data_questions = {
        "test_id": test["id"],
        "content": "Кто ты?"
    }

    response_create = post_something(
        questions_routes['create_questions']['url'],
        headers=headers_data,
        json=data_questions
    )

    assert response_create.status_code == 201
    created_questions = response_create.json()['question']

    yield {
        'id': created_questions['id'],
        'test_id': created_questions['test_id'],
        'content': created_questions['content']
    }

    delete_response = delete_something(
        questions_routes['delete_questions']['url'].replace(':id', created_questions['id']),
        headers=headers_data
    )
    assert delete_response.status_code in [200, 204, 404]