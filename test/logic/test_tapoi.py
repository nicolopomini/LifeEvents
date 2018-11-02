from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase

from logic.tapoi import TapoiConnection, YearInWeeksComputation
from tapoi.api.common import TapoiNotFoundApiException


class TestConnections(TestCase):

    def test_tapoi_connection(self):
        try:
            TapoiConnection.get_connection()
        except TapoiNotFoundApiException as e:
            self.fail("Raised exception " + str(e))


class TestComputation(TestCase):
    def test_correct_computation(self):
        try:
            instance = "866110f3-4b1b-4a56-834b-fa3d39eea4ec"
            asset = "f4646a37-c66e-3993-9f68-3a9e0e9a0793"
            year = 2017
            computator = YearInWeeksComputation(instance, asset, year)
            yiw = computator.get_computation()
            self.assertEqual(len(yiw.get_all_weeks()), 52)
        except Exception:
            self.fail("Something went wrong")

    def test_wrong_computation(self):
        try:
            computator = YearInWeeksComputation("cose a caso", "altre cose a caso", 2017)
            computator.get_computation()
            self.fail("There should by something wrong, but there's not")
        except Exception:
            self.assertTrue(True)
