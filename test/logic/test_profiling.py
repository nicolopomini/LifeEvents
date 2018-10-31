from __future__ import absolute_import
from __future__ import annotations

from typing import List
from unittest import TestCase

from logic.profiling import DetectionInWeeks, WeekProfiling
from models.classifier import SimpleClassifiedYear


class TestProfiling(TestCase):

    def test_profiling(self):
        year = SimpleClassifiedYear()
        year.with_week(1, True)
        for i in range(2, 10):
            year.with_week(i, False)
        year.with_week(10, True)
        for i in range(11, 40):
            year.with_week(i, False)
        year.with_week(40, True)
        for i in range(41, 53):
            year.with_week(i, False)
        profiler = WeekProfiling(year)
        detection: List[DetectionInWeeks] = profiler.analyze()
        expected: List[DetectionInWeeks] = [DetectionInWeeks(1, 10), DetectionInWeeks(40, 40)]
        self.assertEqual(expected, detection)

    def test_empty(self):
        year = SimpleClassifiedYear()
        for i in range(1, 53):
            year.with_week(i, False)
        profiler = WeekProfiling(year)
        detection: List[DetectionInWeeks] = profiler.analyze()
        expected: List[DetectionInWeeks] = []
        self.assertEqual(expected, detection)

    def test_uncomplete(self):
        year = SimpleClassifiedYear()
        for i in range(1, 20):
            year.with_week(i, False)
        profiler = WeekProfiling(year)
        detection: List[DetectionInWeeks] = profiler.analyze()
        expected: List[DetectionInWeeks] = []
        self.assertEqual(expected, detection)