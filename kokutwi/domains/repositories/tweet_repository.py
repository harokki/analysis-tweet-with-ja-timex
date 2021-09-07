from abc import ABCMeta, abstractmethod
from typing import List

from kokutwi.domains.models.tweet import Tweet


class TweetRepository(metaclass=ABCMeta):
    @abstractmethod
    def find_by_user_id(self, user_id: str) -> List[Tweet]:
        raise NotImplementedError
