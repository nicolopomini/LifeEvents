from __future__ import absolute_import
from __future__ import annotations

from typing import Dict, List


class YearInWeeks:
    """
    Class that represents a year of a user aggregated in weeks
    Each key represent the week (from 1 to 52 inclusive)
    Each value is a dict, indicated an entity as key and the number of times the entity was found as value
    """

    def __init__(self) -> None:
        self._weeks: Dict[int, Dict[str, int]] = {}

    def with_week(self, week: int, data: Dict[str, int]) -> None:
        """
        Add a week to the collection
        :param week: number of the week (1 <= week <= 52)
        :param data: the aggregated week: entity => count
        """
        if week < 1 or week > 52:
            raise ValueError("Week number invalid")
        self._weeks[week] = data

    def get_week(self, week: int) -> Dict[str, int]:
        """
        Get the aggregated week: entity => count for the given week
        :param week: number of the week
        :return: the aggregated week: entity => count
        """
        if week < 1 or week > 52:
            raise ValueError("Week number invalid")
        return self._weeks[week]

    def get_all_weeks(self) -> Dict[int, Dict[str, int]]:
        """
        Get all weeks
        :return: a dictionary with all weeks
        """
        return self._weeks

    def to_list(self) -> List[Dict[str, int]]:
        """
        Get a list containing all the weeks of the YearInWeeks instance
        :return: list containing aggregated weeks
        """
        l: List[Dict[str, int]] = []
        for k, v in self._weeks.keys():
            l.append(self._weeks[k])
        return l

    def __iter__(self) -> YearInWeeks:
        self._iter_keys: List[int] = list(self._weeks.keys())
        return self

    def __next__(self):
        try:
            key = self._iter_keys.pop()
            return self._weeks[key]
        except IndexError:
            raise StopIteration

    def __repr__(self):
        return self._weeks.__repr__()