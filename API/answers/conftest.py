import pytest
from BASE.something import post_something, delete_something
from API.auths.conftest import *
from API.tests.conftest import create_delete_tests
from API.questions.conftest import create_delete_questions
from API.answers.answers_routes import answers_routes
from API.answers.AnswersClass import BaseAnswers

@pytest.fixture(scope='session')
def create_delete_answers(get_access_token_admin, create_delete_tests, create_delete_questions):
    test = create_delete_tests
    questions = create_delete_questions

    headers_data = {'x-access-token': f'{get_access_token_admin}'}
    answers_data = BaseAnswers(test['id'], questions['questions_id'])
    answers_dict = answers_data.as_dict()

    data = {
        "test_id": test["id"],
        "question_id": questions["question_id"],
        "first_answer": answers_dict["first_answer"],
        "second_answer": answers_dict["second_answer"],
        "third_answer": answers_dict["third_answer"],
        "fourth_answer": answers_dict["fourth_answer"],
        "true_answer": answers_dict["true_answer"],
    }

    response = post_something(
        answers_routes['create_answers']['url'],
        headers=headers_data,
        json=data,
    )

    assert response.status_code == 201
    created_answer = response.json()["new_answers"]

    yield {
        'id': created_answer["id"],
        'question_id': created_answer["question_id"],
        'first_answer': created_answer["first_answer"],
        'second_answer': created_answer["second_answer"],
        'third_answer': created_answer["third_answer"],
        'fourth_answer': created_answer["fourth_answer"],
        'true_answer': created_answer["true_answer"],
    }

    delete_response = delete_something(
        answers_routes['delete_answer']['url'].replace(':id', created_answer["id"]),
        headers=headers_data,
    )

    assert delete_response.status_code in [200, 204, 404]