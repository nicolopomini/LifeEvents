from __future__ import absolute_import
from __future__ import annotations

from typing import List
# from dateutil import parser


class Tweet:
    def __init__(self, created: str, id: int, full_text: str, favorite_count: int, hashtags: List[str], lang: str,
                 media: List[str], retweet_count: int, urls: List[str]):
        self.created = created  # data di creazione del tweet
        self.id = id  # id del tweet
        self.full_text = full_text  # testo del tweet
        self.favorite_count = favorite_count  # numero di favoriti
        self.hashtags = hashtags  # array di hashtags
        self.lang = lang  # lingua
        self.media = media  # array di url
        self.retweet_count = retweet_count  # numero di retweet
        self.urls = urls  # array di url

    def __repr__(self):
        return 'Tweet(id = {id},' \
               ' created = {created},' \
               ' text = {text},' \
               ' favorite_count = {fav},' \
               ' retweet_count = {ret},' \
               ' lang = {lang})'.format(
                    id=self.id,
                    created=self.created,
                    text=self.full_text,
                    ret=self.retweet_count,
                    fav=self.favorite_count,
                    lang=self.lang
                )
