import pytest

from kokutwi.domains.models.tweet import EventTweet, Tweet


def test_initialize_event_tweet():
    event_tweet = EventTweet("aaaa")

    assert event_tweet.tweet == "aaaa"


def test_initialize_tweet():
    tweet = Tweet(1234, "https://twitter.com/user_id/status/1234", "ツイートです", "user")

    assert tweet.id == 1234
    assert tweet.link == "https://twitter.com/user_id/status/1234"
    assert tweet.tweet == "ツイートです"
    assert tweet.user_id == "user"
