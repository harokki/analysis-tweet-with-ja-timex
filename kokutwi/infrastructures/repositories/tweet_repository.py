from typing import List

import twint

from kokutwi.domains.models.tweet import Tweet, TwintBase
from kokutwi.domains.repositories.tweet_repository import TweetRepository


def convert_tweet(x):
    return Tweet(tweet_id=x.id, link=x.link, tweet=x.tweet, user_id=x.username)


class TweetRepositoryWithTwint(TweetRepository):
    def find_by_user_id(self, user_id: str) -> List[Tweet]:
        twint_base = TwintBase()
        c = twint_base.config
        c.Username = user_id

        # これをしないと前回の結果が残ってしまうことがある
        twint.output.clean_lists()

        twint.run.Search(c)
        tweets = twint.output.tweets_list
        tweets_map = list(map(convert_tweet, tweets))

        return tweets_map
