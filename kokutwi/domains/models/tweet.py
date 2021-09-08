from dataclasses import dataclass

from twint import Config


@dataclass
class Tweet:
    tweet_id: int
    link: str
    tweet: str
    user_id: str


@dataclass
class TwintBase:
    config = Config(Store_object=True, Hide_output=True)
