import pytest

from analysis_tweet.infrastructures.repositories.tweet_repository import (
    TweetRepositoryWithTwint,
)


def test_find_by_user_id():
    repository = TweetRepositoryWithTwint()
    result = repository.find_by_user_id("test")

    assert result[0].tweet == "aaaa"
