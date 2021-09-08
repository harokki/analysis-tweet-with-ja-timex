from unittest import mock

import pytest
from fastapi.testclient import TestClient

from kokutwi.application import app
from kokutwi.domains.models.tweet import Tweet
from kokutwi.infrastructures.repositories.tweet_repository import (
    TweetRepositoryWithTwint,
)


@pytest.fixture
def client():
    yield TestClient(app)


def test_get_event_tweets_by_id(client):
    repository_mock = mock.Mock(spec=TweetRepositoryWithTwint)
    repository_mock.find_by_user_id.return_value = [
        Tweet(1234, "https://1234", "これはツイート", "user"),
        Tweet(1235, "https://1235", "これは9月2日のツイート", "user"),
        Tweet(1236, "https://1236", "これは9月2日 16:00のツイート", "user"),
    ]

    with app.container.tweet_repository.override(repository_mock):
        response = client.get("/tweets/user")

    data = response.json()

    assert response.status_code == 200
    assert data == {
        "user_id": "user",
        "tweets": [
            {
                "tweet_id": 1236,
                "link": "https://1236",
                "tweet": "これは9月2日 16:00のツイート",
                "user_id": "user",
            }
        ],
    }
