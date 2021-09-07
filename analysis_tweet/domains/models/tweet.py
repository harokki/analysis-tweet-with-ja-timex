from dataclasses import dataclass
from datetime import datetime
import os


@dataclass
class EventTweet:
    tweet: str


@dataclass
class Tweet:
    id: int
    link: str
    tweet: str
    user_id: str
