from typing import List

from analysis_tweet.domains.repositories.tweet_repository import TweetRepository
from analysis_tweet.domains.models.event_tweet import EventTweet


class TweetService:
    def __init__(self, tweet_repository: TweetRepository) -> None:
        self._repository = tweet_repository

    def get_tweet_by_user_id(self, user_id: str) -> List[EventTweet]:
        return self._repository.find_by_user_id(user_id)
