import pytest
from news_routes import news_routes
from BASE.something import post_something, get_something
from NewsClass import BaseNews

# создание новости, по сути это и есть позитивный тест-кейс
@pytest.fixture(scope="session")
def created_news(get_access_token_admin):
    headers_data = {"x-access-token": f"{get_access_token_admin}"}
    news = BaseNews()
    response = post_something(
        news_routes["create_news"]["url"],
        headers=headers_data,
        json=news.as_dict()
    )
    assert response.status_code == 201
    return news

@pytest.fixture(scope="session")
def get_news_by_id(id=13):
    response = get_something(
        news_routes["get_news_by_id"]["url"].replace(":id", str(id)),
    )
    assert response.status_code == 200
    return response.json()