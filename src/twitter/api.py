from __future__ import absolute_import
from __future__ import annotations

import twitter as tw

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

    def get_tweet(self, tweet_id: int):
        return self._api.GetStatus(tweet_id)

t = TwitterAPI()
print(t.get_tweet(1051603095589933059))