import allure
import pytest

from API.news.news_routes import news_routes
from BASE.something import *
from articles_routes import articles_routes
from API.auths.conftest import get_access_token_admin
from ArticlesClass import articles_data_dict

negative_cases = [
    ('title', ' ', 400),
    ('title', None, 400),
    ('content', ' ', 400),
    ('content', None, 400),
    ('image', {}, 400),
    ('file', {}, 400),
]

class TestArticles:
    @allure.title("negative articles create tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_create_articles(self, field, value, articles_data_dict, get_access_token_admin, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}
        data = {
            'title': articles_data_dict['title'],
            'content': articles_data_dict['content'],
            'image': articles_data_dict['image'],
            'file': articles_data_dict['file'],
        }
        data[field] = value
        response = post_something(
            articles_routes["create_articles"]["url"],
            headers=headers_data,
            json=data
        )
        assert response.status_code == expected_status
        assert response.json().get('message') == "Validation error!"

    @allure.title("Negative articles get tests")
    @pytest.mark.parametrize("id, expected_status", [
        (0, 400),
        ('str', 400),
        ('%', 400),
        (1000001, 404)
    ])
    def test_negative_get_articles_by_id(self, id, expected_status, get_access_token_admin):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}

        response = get_something(
            articles_routes['get_articles_by_id']['url'].replace(":id", str(id)),
            #headers=headers_data
        )
        assert response.status_code == expected_status

    @allure.title("Negative articles edit tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_edit_articles_by_id(self, get_access_token_admin, field, create_articles, value, expected_status):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}
        articles_id = create_articles['id']
        articles_data = create_articles['data'].copy()

        articles_data[field] = value

        response = patch_something(
            articles_routes["edit_articles"]["url"].replace(":id", str(articles_id)),
            headers=headers_data,
            json=articles_data
        )

        assert response.status_code == expected_status
        assert response.json()

    @allure.title("Negative articles delete tests")
    @pytest.mark.parametrize("id, expected_status", [
        (0, 400),
        ('str', 400),
        ('%', 400),
        (1000001, 404)
    ])
    def test_negative_delete_articles(self, id, expected_status, get_access_token_admin):
        headers_data = {'x-access-token': f'{get_access_token_admin}'}
        response = delete_something(
            articles_routes["delete_articles"]["url"].replace(":id", str(id)),
            headers=headers_data
        )
        assert response.status_code == expected_status
        assert response.json()