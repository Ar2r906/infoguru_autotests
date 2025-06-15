import pytest
from news_routes import news_routes
from BASE.something import post_something
from NewsClass import TestNews

# создание новости, по сути это и есть позитивный тест-кейс
@pytest.fixture(scope="session")
def created_news(get_access_token_admin):
    headers_data = {'x-access-token': f'{get_access_token_admin}'}
    news = TestNews()
    response = post_something(
        news_routes["create_news"]["url"],
        headers=headers_data,
        json=news.as_dict()
    )
    assert response.status_code == 201
    return news