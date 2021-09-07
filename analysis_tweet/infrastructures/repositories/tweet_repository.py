from typing import List
import twint

from analysis_tweet.domains.repositories.tweet_repository import TweetRepository
from analysis_tweet.domains.models.tweet import EventTweet, Tweet


def convert_tweet(x):
    return Tweet(id=x.id, link=x.link, tweet=x.tweet, user_id=x.username)


class TweetRepositoryWithTwint(TweetRepository):
    def find_by_user_id(self, user_id: str) -> List[Tweet]:
        c = twint.Config()
        c.Username = user_id
        c.Limit = 1
        c.Store_object = True
        c.Hide_output = True

        twint.output.clean_lists()
        twint.run.Search(c)
        tweets = twint.output.tweets_list
        tweets_map = list(map(convert_tweet, tweets))

        return tweets_map
