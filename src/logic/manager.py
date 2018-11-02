from __future__ import absolute_import
from __future__ import annotations

from typing import List

from classifier.decision_tree import SimpleWeddingDecisionTree, SimpleBirthDecisionTree
from logic.profiling import WeekProfiling, DetectionInWeeks
from logic.tapoi import YearInWeeksComputation


class Manager:
    """
    This class handles the whole computation process
    From asking Tapoi the entities
    to the classification
    and finally the analysis of the timeline
    """
    LIFE_EVENTS = ['wedding', 'birth']

    @staticmethod
    def compute_week_profiling(instance: str, asset: str, year: int, life_event: str) -> List[DetectionInWeeks]:
        """
        Create a manager of the entire process
        :param instance: the instance of the analysis
        :param asset: the asset of the analysis
        :param year: the year of the analysis
        :param life_event: the life event of the analysis
        :return a list of time ranges with detections
        """
        if life_event not in Manager.LIFE_EVENTS:
            raise ValueError("Life event %s not defined" % life_event)
        computator = YearInWeeksComputation(instance, asset, year)
        year_in_weeks = computator.get_computation()
        if life_event == 'wedding':
            classifier = SimpleWeddingDecisionTree()
        else:
            classifier = SimpleBirthDecisionTree()
        classifier.fit()
        classified_year = classifier.predict(year_in_weeks)
        profiler = WeekProfiling(classified_year)
        detections: List[DetectionInWeeks] = profiler.analyze()
        return detections

# TapoiNotFoundApiException 404 istanza o asset non esistono