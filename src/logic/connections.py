from __future__ import absolute_import
from __future__ import annotations

import json

from tapoi.tapoi import Tapoi


class TapoiConnection:

    @staticmethod
    def get_connection() -> Tapoi:
        keys = None
        with open('keys.json') as f:
            keys = json.load(f)
        return Tapoi(keys["key"], keys["secret"])

TapoiConnection.get_connection()