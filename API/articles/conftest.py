import pytest
from articles_routes import articles_routes
from BASE.something import *
from ArticlesClass import BaseArticles

@pytest.fixture(scope="session")
def create_articles(get_access_token_admin):
    headers_data = {"x-access-token": f"{get_access_token_admin}"}
    articles = BaseArticles()

    response = post_something(
        articles_routes["create_articles"]["url"],
        headers=headers_data,
        json=articles.as_dict(),
    )

    assert response.status_code == 201
    created = response.json()["newArticle"]

    yield {
        "id": created["id"],
        "data": articles.as_dict(),
    }

    delete_response = delete_something(
        articles_routes["delete_articles"]["url"].replace(":id", str(created["id"])),
        headers=headers_data
    )
    assert delete_response.status_code in [200, 204, 404]
