import pytest

from analysis_tweet.infrastructures.repositories.tweet_repository import (
    TweetRepositoryWithTwint,
)


def test_find_by_user_id():
    repository = TweetRepositoryWithTwint()
    results = repository.find_by_user_id("rokki188")

    assert results[0].id
    assert results[0].tweet
    assert results[0].link
    assert results[0].user_id == "rokki188"
