from __future__ import absolute_import
from __future__ import annotations

from unittest import TestCase

from classifier.decision_tree import SimpleWeddingDecisionTree, SimpleBirthDecisionTree
from models.classifier import SimpleClassifiedYear
from models.tapoi import YearInWeeks


class TestTraining(TestCase):
    def test_training(self):
        try:
            tree = SimpleWeddingDecisionTree()
            tree.fit()
        except Exception as e:
            self.fail("Something went wrong: " + str(e))


class TestPredictions(TestCase):
    def test_prediction(self):
        yiw = YearInWeeks()
        yiw.with_week(1, {
            "": 1,
            ",": 12,
            ".": 56
        })
        tree = SimpleBirthDecisionTree()
        tree.fit()
        scy: SimpleClassifiedYear = tree.predict(yiw)
        self.assertFalse(scy.get_week(1))
