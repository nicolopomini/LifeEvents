from __future__ import absolute_import
from __future__ import annotations

from typing import List

import twitter as tw

from src.models.twitter import Tweet
from src.twitter.common import Keys


class TwitterAPI:
    def __init__(self) -> None:
        # Full tweet texts
        # sleeps in case max request number is reached
        self._api = tw.Api(Keys.CONSUMER_KEY,
                           Keys.CONSUMER_SECRET,
                           Keys.ACCESS_KEY,
                           Keys.ACCESS_SECRET,
                           tweet_mode='extended',
                           sleep_on_rate_limit=True)

    def _parse_tweet(self, tweet) -> Tweet:
        hashtags = tweet.hashtags
        if hashtags is None:
            hashtags = []
        media = tweet.media
        if media is None:
            media = []
        urls = tweet.urls
        if urls is None:
            urls = []
        return Tweet(tweet.created_at, tweet.id, tweet.full_text, tweet.favorite_count, hashtags, tweet.lang,
                     media, tweet.retweet_count, urls)

    def get_tweet(self, tweet_id: int):
        tweet = self._api.GetStatus(tweet_id)
        return self._parse_tweet(tweet)

    def get_tweet_list(self, ids: List[int]) -> List[Tweet]:
        rtr = []
        tweets = self._api.GetStatuses(ids)
        for t in tweets:
            rtr.append(self._parse_tweet(t))
        return rtr
