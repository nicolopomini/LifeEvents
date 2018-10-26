from __future__ import absolute_import
from __future__ import annotations

from typing import List
from dateutil import parser
from datetime import datetime


class Tweet:
    """
    Class that represents a Tweet
    """
    def __init__(self, created: str, id: int, full_text: str, favorite_count: int, hashtags: List[str], lang: str,
                 media: List[str], retweet_count: int, urls: List[str]):
        """
        Create an instance of a tweet
        :param created: string of the date of creation
        :param id: numerical id of the tweet
        :param full_text: text of the tweet
        :param favorite_count: number of favourites the tweet has received
        :param hashtags: array of strings containing the hashtags that are in the text of the tweet
        :param lang: language with which the tweet is written
        :param media: links to the media attached to the tweet
        :param retweet_count: number of retweets the tweet has received
        :param urls: array of external links the tweet contains
        """
        self.created: datetime = parser.parse(created)  # data di creazione del tweet
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

    def __eq__(self, o: Tweet) -> bool:
        return self.id == o.id

    def __lt__(self, other: Tweet) -> bool:
        return self.id < other.id

    def __gt__(self, other: Tweet) -> bool:
        return self.id > other.id

