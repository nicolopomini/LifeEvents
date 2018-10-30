from __future__ import absolute_import
from __future__ import annotations

import json

from tapoi.tapoi import Tapoi
import os

TEST_FILENAME = os.path.join(os.path.dirname(__file__), 'test.txt')

class TapoiConnection:

    @staticmethod
    def get_connection() -> Tapoi:
        KEYS_FILE = os.path.join(os.path.dirname(__file__), 'keys.json')
        keys = None
        with open(KEYS_FILE) as f:
            keys = json.load(f)
        return Tapoi(keys["key"], keys["secret"])
