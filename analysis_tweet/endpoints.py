from fastapi import APIRouter, Depends, Response, status
from dependency_injector.wiring import inject, Provide

from analysis_tweet.containers import Container
from analysis_tweet.services.tweet_service import TweetService

router = APIRouter()


@router.get("/tweets/{user_id}")
@inject
def get_by_id(
    user_id: str,
    tweet_service: TweetService = Depends(Provide[Container.tweet_service]),
):
    return tweet_service.get_event_tweets_by_user_id(user_id)
