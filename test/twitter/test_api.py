from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase

from src.twitter.api import TwitterAPI


class TestTweetFetch(TestCase):

    def test_single_fetch(self):
        api = TwitterAPI()
        id = 1051603095589933059
        tweet = api.get_tweet(id)
        self.assertEqual(tweet.id, id)

    def test_list_fetch(self):
        ids = [1054432979555151872, 1026579130312257541, 984780707464663040]
        api = TwitterAPI()
        tweets = api.get_tweet_list(ids)
        equals = True
        for i, j in zip(ids, tweets):
            if i != j.id:
                equals = False
        self.assertEqual(equals, True)