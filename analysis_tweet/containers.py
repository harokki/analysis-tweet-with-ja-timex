from dependency_injector import containers, providers

from analysis_tweet.infrastructures.repositories.tweet_repository import (
    TweetRepositoryWithTwint,
)
from analysis_tweet.services.tweet_service import TweetService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    tweet_repository = providers.Factory(TweetRepositoryWithTwint)

    tweet_service = providers.Factory(TweetService, tweet_repository=tweet_repository)
