from dependency_injector import containers, providers

from kokutwi.infrastructures.repositories.tweet_repository import (
    TweetRepositoryWithTwint,
)
from kokutwi.services.tweet_service import TweetService


class Container(containers.DeclarativeContainer):
    config = providers.Configuration()

    tweet_repository = providers.Factory(TweetRepositoryWithTwint)

    tweet_service = providers.Factory(TweetService, tweet_repository=tweet_repository)
