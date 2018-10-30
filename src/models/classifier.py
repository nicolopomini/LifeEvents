from __future__ import absolute_import
from __future__ import annotations

from typing import Dict, List


class ClassifiedWeek:
    """
    Class that represent a week classified by the classifier
    It contains a list of triple:
    - the Wikipedia entity
    - its classification
    - the counter of how many times it was used in this week
    """

    def __init__(self) -> None:
        """
        Instantiate a new ClassifiedWeek
        """
        # URI => (classification, count)
        self._list: Dict[str, (bool, int)] = {}

    def with_entitiy(self, uri: str, classification: bool, count: int) -> None:
        """
        Add a classified entity to the list
        :param uri: the URI that identifies the entity
        :param classification: the result of the classification
        :param count: counter of how many times the entity was found in the week
        """
        if uri in self._list:
            old_counter = self._list[uri][1]
            new_counter = old_counter + count
            new_classification = classification and self._list[uri][0]
            self._list[uri] = (new_classification, new_counter)
        else:
            self._list[uri] = (classification, count)

    def get_entity(self, uri: str) -> (bool, int):
        """
        Get the specified Wikipedia entity
        :param uri: the URI that identifies the entity
        :return: a couple classification, counter for the entity
        """
        if uri in self._list:
            return self._list[uri][0], self._list[uri][1]
        else:
            raise ValueError("The URI %s does not exist in this week" % uri)


class ClassifiedYear:
    """
    Class that represent a year classified by the classifier.
    It contains:
    - the week numbers
    - the associated ClassifiedWeek
    """

    def __init__(self) -> None:
        """
        Istantiate a new ClassifiedYear
        """
        self._weeks: Dict[int, ClassifiedWeek] = {}

    def with_week(self, week_number: int, classification: ClassifiedWeek) -> None:
        """
        Add a classified week to the list
        :param week_number: number of the week (from 1 to 52 inclusive)
        :param classification: the relative ClassifiedWeek
        """
        if week_number < 1 or week_number > 52:
            raise ValueError("Week number invalid")
        self._weeks[week_number] = classification

    def get_week(self, week_number: int) -> ClassifiedWeek:
        """
        Get a specific week
        :param week_number: number of the week
        :return: the relative ClassifiedWeek
        """
        if week_number < 1 or week_number > 52:
            raise ValueError("Week number invalid")
        if week_number not in self._weeks:
            raise ValueError("The week %d does not exist" % week_number)
        return  self._weeks[week_number]


class SimpleClassifiedYear:
    """
    Class that contains a list of weeks, each one represented by a boolean indicator,
    that tells whether in that week the user has spoken about the life event
    """

    def __init__(self) -> None:
        self._weeks: Dict[int, bool] = {}

    def with_week(self, week_number: int, classification: bool) -> None:
        self._weeks[week_number] = classification

    def get_week(self, week_number: int) -> bool:
        if week_number < 1 or week_number > 52:
            raise ValueError("Week number invalid")
        if week_number not in self._weeks:
            raise ValueError("The week %d does not exist" % week_number)
        return  self._weeks[week_number]

    def __iter__(self) -> SimpleClassifiedYear:
        self._iter_keys: List[int] = list(self._weeks.keys())
        return self

    def __next__(self):
        try:
            key = self._iter_keys.pop()
            return self._weeks[key]
        except IndexError:
            raise StopIteration