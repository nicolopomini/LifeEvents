from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase

from logic.connections import TapoiConnection
from tapoi.api.common import TapoiNotFoundApiException


class TestConnections(TestCase):

    def test_tapoi_connection(self):
        try:
            TapoiConnection.get_connection()
        except TapoiNotFoundApiException as e:
            self.fail("Raised exception " + str(e))