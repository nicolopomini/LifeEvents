from __future__ import absolute_import
from __future__ import annotations

import json

from models.tapoi import YearInWeeks
from tapoi.api.common import TapoiNotFoundApiException
from tapoi.object.computation.activity import EntityMapComputation
from tapoi.tapoi import Tapoi
import os


class TapoiConnection:

    @staticmethod
    def get_connection() -> Tapoi:
        """
        Get a connection object with Tapoi
        :return: the connection with Tapoi
        """
        KEYS_FILE = os.path.join(os.path.dirname(__file__), 'keys.json')
        keys = None
        with open(KEYS_FILE) as f:
            keys = json.load(f)
        return Tapoi(keys["key"], keys["secret"])


class ComputationByYearManager:
    """
    This class deals with asking Tapoi a computation for a given couple instance, asset
    """

    def __init__(self, instance: str, asset: str, year: int) -> None:
        """
        Create the manager
        :param instance: the instance of the computation to be requested
        :param asset: the asset of the computation to be requested
        :param year: the year of the computation to be requested
        """
        self.tapoi = TapoiConnection.get_connection()
        self.instance = instance
        self.asset = asset
        self.year = year

    def get_computation(self):
        """
        Get a computation by Tapoi
        """
        raise Exception("Method ComputationByYearManager.get_computation() not implemented yet")


class YearInWeeksComputation(ComputationByYearManager):
    """
    Analyze a solar year week by week
    """

    def __init__(self, instance: str, asset: str, year: int) -> None:
        """
        Create the analyzer
        :param instance: instance: the instance of the computation to be requested
        :param asset: the asset of the computation to be requested
        :param year: the year of the computation to be requested
        """
        super().__init__(instance, asset, year)

    def get_computation(self) -> YearInWeeks:
        """
        Get a year week by week, and for each week the list of entities is given
        :return: a YearInWeeks with all the entities for each week
        """
        # check if instance and asset exist
        try:
            self.tapoi.interface.instance.get(self.instance)
            self.tapoi.interface.asset.get(self.instance, self.asset)
            year = YearInWeeks()
            # for each week of the year
            for i in range(1, 53):
                computation = EntityMapComputation.allActivities()
                computation.withAssetTarget(self.instance, self.asset)
                computation.withWeekPeriod(self.year, i)
                try:
                    c = self.tapoi.interface.computation.get(computation).getData().get_dictionary()
                    year.with_week(i, c)
                except TapoiNotFoundApiException:  # empty week
                    year.with_week(i, {})
            return year
        except TapoiNotFoundApiException:
            print("Error, instance of asset don't exist")
