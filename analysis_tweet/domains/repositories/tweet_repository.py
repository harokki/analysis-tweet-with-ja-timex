from abc import ABCMeta, abstractmethod
from typing import List

from analysis_tweet.domains.models.event_tweet import EventTweet


class TweetRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_user_name(self, user_name: str) -> List[EventTweet]:
        raise NotImplementedError
