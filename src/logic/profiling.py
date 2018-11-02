from __future__ import absolute_import
from __future__ import annotations

from typing import List

from models.classifier import SimpleClassifiedYear


class Detection:
    """
    Class that represents a single generic profilation
    """

    def __init__(self, start, finish) -> None:
        """
        Define a new detection
        :param start: when the detection starts
        :param finish: when the detection ends
        """
        self.start = start
        self.finish = finish

    def to_repr(self) -> dict:
        return {
            "from": self.start,
            "to": self.finish
        }


class DetectionInWeeks(Detection):
    """
    Detection among weeks
    """

    def __init__(self, start: int, finish: int) -> None:
        """
        Create a new detection among weeks
        :param start: starting week
        :param finish: final week
        """
        if start < 1 or start > 52:
            raise ValueError("Start is a week number invalid")
        if finish < 1 or finish > 52:
            raise ValueError("Finish is a week number invalid")
        super().__init__(start, finish)

    def __repr__(self) -> str:
        return "DetectionInWeeks(from: %d, to %d)" % (self.start, self.finish)

    def __eq__(self, o: DetectionInWeeks) -> bool:
        return self.start == o.start and self.finish == o.finish


class WeekProfiling:
    MAX_PERIOD = 26     # in weeks

    def __init__(self, year_in_weeks: SimpleClassifiedYear) -> None:
        self.year_in_weeks = year_in_weeks

    def analyze(self) -> List[DetectionInWeeks]:
        """
        Analyze the entire year grouped by weeks, in order to find any possible life event
        :return: a list of detections
        """
        detections: List[DetectionInWeeks] = []
        start = 100
        end = 0
        for week, classification in self.year_in_weeks:
            # in case the week is classified as related with the LE
            if classification:
                if week < start:
                    # is the first "positive" week
                    start = week
                    end = week
                elif week - end < WeekProfiling.MAX_PERIOD:
                    # is not the first positive week encountered,
                    # and it is the case that is not too far away from the previous positive one
                    end = week
                else:
                    # this positive week is too far away from the previous one:
                    # let's close the previous detection and start a new one
                    detections.append(DetectionInWeeks(start, end))
                    start = week
                    end = week
        # finally, if there is an open interval, save it
        if start <= end:
            detections.append(DetectionInWeeks(start, end))
        return detections
