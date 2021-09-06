from dataclasses import dataclass
from datetime import datetime
import os


@dataclass
class EventTweet:
    tweet: str
