import pytest
from news_routes import news_routes
from BASE.something import post_something, get_something, delete_something
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
    created = response.json()

    yield {
        "id": created["id"],
        "headers": headers_data,
        "data": news.as_dict()
    }

    delete_response = delete_something(
        news_routes["delete_news"]["url"].replace(":id", str(created["id"])),
        headers=headers_data
    )
    assert delete_response.status_code in [200, 204]