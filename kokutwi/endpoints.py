from typing import List

from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide
from pydantic import BaseModel

from kokutwi.containers import Container
from kokutwi.services.tweet_service import TweetService
from kokutwi.domains.models.tweet import Tweet

router = APIRouter()


class EventTweetResponse(BaseModel):
    user_id: str
    tweets: List[Tweet]


@router.get("/tweets/{user_id}", response_model=EventTweetResponse)
@inject
def get_event_tweets_by_id(
    user_id: str,
    tweet_service: TweetService = Depends(Provide[Container.tweet_service]),
):
    event_tweets = tweet_service.get_event_tweets_by_user_id(user_id)

    return {"user_id": user_id, "tweets": event_tweets}
