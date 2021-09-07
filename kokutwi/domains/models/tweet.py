import os
from dataclasses import dataclass
from datetime import datetime

from twint import Config


@dataclass
class EventTweet:
    tweet: str


@dataclass
class Tweet:
    id: int
    link: str
    tweet: str
    user_id: str


@dataclass
class TwintBase:
    config = Config(Store_object=True, Hide_output=True)
