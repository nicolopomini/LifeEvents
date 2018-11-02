from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase

from logic.manager import Manager
from tapoi.api.common import TapoiNotFoundApiException


class TestManager(TestCase):
    def test_wedding_errors(self):
        try:
            instance = "866110f3-4b1b-4a56-834b-fa3d39eea4ec"
            asset = "f4646a37-c66e-3993-9f68-3a9e0e9a0793"
            year = 2017
            detections = Manager.compute_week_profiling(instance, asset, year, 'wedding')
        except Exception:
            self.fail("Something went wrong")

    def test_birth_errors(self):
        try:
            instance = "866110f3-4b1b-4a56-834b-fa3d39eea4ec"
            asset = "f4646a37-c66e-3993-9f68-3a9e0e9a0793"
            year = 2017
            detections = Manager.compute_week_profiling(instance, asset, year, 'birth')
        except Exception:
            self.fail("Something went wrong")

    def test_unexisting_entity(self):
        try:
            instance = "bla bla bla"
            asset = "bla bla"
            year = 2017
            detections = Manager.compute_week_profiling(instance, asset, year, 'birth')
            self.fail("Something should be wrong, but it isn't")
        except TapoiNotFoundApiException:
            self.assertTrue(True)

    def test_unexisting_year(self):
        instance = "866110f3-4b1b-4a56-834b-fa3d39eea4ec"
        asset = "f4646a37-c66e-3993-9f68-3a9e0e9a0793"
        year = -1
        detections = Manager.compute_week_profiling(instance, asset, year, 'wedding')
        self.assertEqual(detections, [])

    def test_unexisting_lifeevent(self):
        try:
            instance = "866110f3-4b1b-4a56-834b-fa3d39eea4ec"
            asset = "f4646a37-c66e-3993-9f68-3a9e0e9a0793"
            year = 2017
            detections = Manager.compute_week_profiling(instance, asset, year, 'fuffa')
            self.fail("Something should be wrong, but it isn't")
        except ValueError:
            self.assertTrue(True)