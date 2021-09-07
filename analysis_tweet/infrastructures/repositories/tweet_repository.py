from typing import List

from analysis_tweet.domains.repositories.tweet_repository import TweetRepository
from analysis_tweet.domains.models.event_tweet import EventTweet


class TweetRepositoryWithTwint(TweetRepository):
    def find_by_user_id(self, user_name: str) -> List[EventTweet]:
        return [EventTweet("aaaa")]
