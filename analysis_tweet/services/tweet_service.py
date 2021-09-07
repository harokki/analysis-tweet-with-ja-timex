from typing import List
from ja_timex import TimexParser

from analysis_tweet.domains.repositories.tweet_repository import TweetRepository
from analysis_tweet.domains.models.tweet import Tweet


class TweetService:
    def __init__(self, tweet_repository: TweetRepository) -> None:
        self._repository = tweet_repository

    def get_event_tweets_by_user_id(self, user_id: str) -> List[Tweet]:
        tweets = self._repository.find_by_user_id(user_id)
        event_tweets = []
        for tweet in tweets:
            timexes = TimexParser().parse(tweet.tweet)
            if timexes:
                for timex in timexes:
                    if timex.type == "DATE":
                        event_tweets.append(tweet)
                        break

        return event_tweets
