from kokutwi.domains.models.tweet import Tweet


def test_initialize_tweet():
    tweet = Tweet(1234, "https://twitter.com/user_id/status/1234", "ツイートです", "user")

    assert tweet.tweet_id == 1234
    assert tweet.link == "https://twitter.com/user_id/status/1234"
    assert tweet.tweet == "ツイートです"
    assert tweet.user_id == "user"
