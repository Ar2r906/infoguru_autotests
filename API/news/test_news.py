import pytest
import allure
from BASE.something import *
from news_routes import news_routes
from fixtures import get_access_token_admin, created_news
from NewsClass import *

negative_cases = [
    ('title', ' ', 400),
    ('title', None, 400),
    ('content', ' ', 400),
    ('content', None, 400),
    ('image', {}, 400),
    ('file', {}, 400),
]

class TestNews:
    @allure.description("Negative news create tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_create_news(self, get_access_token_admin, news_data_dict, field, value, expected_status):
        headers_data = {"x-access-token": f"{get_access_token_admin}"}
        news = news_data_dict.copy()
        news[field] = value

        response = post_something(
            news_routes["create_news"]["url"],
            headers=headers_data,
            json=news
        )

        assert response.status_code == expected_status

    @allure.description("Negative news get tests")
    @pytest.mark.parametrize("id, expected_status", [
        (0, 400),
        ('str', 400),
        ('%', 400),
        (10001, 400)
    ])
    def test_negative_get_news_by_id(self, id, expected_status):
        response = get_something(
            news_routes["get_news_by_id"]["url"],
            params={"id": id}
        )
        assert response.status_code == expected_status

    @allure.title("Negative news edit tests")
    @pytest.mark.parametrize("field, value, expected_status", negative_cases)
    def test_negative_edit_news(self, get_access_token_admin, created_news, news_data_dict, field, value, expected_status):

        headers_data = {"x-access-token": f"{get_access_token_admin}"}
        news_id = created_news["id"]
        news_data = created_news["data"]
        news_data[field] = value

        response = patch_something(
            news_routes["edit_news"]["url"],
            headers=headers_data,
            params={"id": news_id},
            json=news_data
        )

        assert response.status_code == expected_status