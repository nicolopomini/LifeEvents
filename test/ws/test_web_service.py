from __future__ import absolute_import
from __future__ import annotations

import json
from unittest import TestCase

from ws.web_service import WebService


class TestLifeEventDiscovery(TestCase):
    def setUp(self):
        ws = WebService()
        self.client = ws._app.test_client()
        super().setUp()

    def test_malformed_request(self):
        post_data = json.dumps({
            "wrong_key": "wrong_value"
        })
        result = self.client.post("/le", data=post_data, content_type="application/json")
        self.assertEqual(400, result.status_code)

    def test_unexisting_entity(self):
        post_data = json.dumps({
            "instance": "wrong_value",
            "asset": "qualcosa",
            "year": 2017,
            "lifeEvent": "wedding"
        })
        result = self.client.post("/le", data=post_data, content_type="application/json")
        self.assertEqual(404, result.status_code)

    def test_unexisting_le(self):
        post_data = json.dumps({
            "instance": "866110f3-4b1b-4a56-834b-fa3d39eea4ec",
            "asset": "f4646a37-c66e-3993-9f68-3a9e0e9a0793",
            "year": 2017,
            "lifeEvent": "vlalb"
        })
        result = self.client.post("/le", data=post_data, content_type="application/json")
        self.assertEqual(422, result.status_code)

    def test_correct(self):
        post_data = json.dumps({
            "instance": "866110f3-4b1b-4a56-834b-fa3d39eea4ec",
            "asset": "f4646a37-c66e-3993-9f68-3a9e0e9a0793",
            "year": 2017,
            "lifeEvent": "wedding"
        })
        result = self.client.post("/le", data=post_data, content_type="application/json")
        self.assertEqual(200, result.status_code)
