from __future__ import absolute_import
from __future__ import annotations

from sklearn.tree import DecisionTreeClassifier, export_graphviz
import os
import json
import numpy as np

from models.classifier import SimpleClassifiedYear
from models.tapoi import YearInWeeks


class DecisionTree:
    """
    Generic class that manage the decision tree
    """
    def __init__(self, dataset_as_path) -> None:
        """
        Instantiate a new decision tree
        :param dataset_as_path: the path of the json used to train the classifier
        """
        self.training_set = dataset_as_path
        self.tree = DecisionTreeClassifier(max_depth=5)
        self._indexes = {}

    def fit(self) -> None:
        """
        Train the classifier
        """
        DATASET_FILE = os.path.join(os.path.dirname(__file__), self.training_set)
        with open(DATASET_FILE) as json_data:
            data = json.load(json_data)
        # delete duplicate records
        unique = {}
        for d in data:
            if d["id"] not in unique:
                unique[d["id"]] = d
        # convert again dataset in a list
        data = []
        for d in unique:
            data.append(unique[d])
        # Create the y array of truths
        y = np.empty((len(data)), dtype=bool)
        for i in range(len(data)):
            y[i] = data[i]['is_about_life_event'] == 'Yes' or data[i]['is_related_life_event'] == 'Yes'
        # create the real training set, considering only those annotations that have a good confidence
        i = 0
        for d in data:
            for annotation in d['annotations']:
                if annotation['confidence'] >= 0.5 and annotation['uri'] not in self._indexes:
                    self._indexes[annotation['uri']] = i
                    i += 1
        X = np.zeros((len(data), len(self._indexes)), dtype=int)
        for i in range(len(data)):
            for annotation in data[i]['annotations']:
                if annotation['confidence'] >= 0.5 and annotation['uri'] in self._indexes:
                    X[i][self._indexes[annotation['uri']]] += 1
        self.tree.fit(X, y)
        """
        features_names = []
        for f in self._indexes.items():
            features_names.append(f[0])
        export_graphviz(self.tree, out_file='tmp.dot', feature_names=features_names,
                        class_names=['False', 'True'])
        """

    def predict(self, data: YearInWeeks):
        """
        Schema to be implemented
        """
        raise Exception("Un-implemented method predict()")


class SimpleDecisionTree(DecisionTree):
    """
    Class that performs the classification in a simple way:
    - one classification for each week
    - does not take count of the entity counter
    So in the end every week will be represented by a boolean label
    """

    def __init__(self, dataset_as_path) -> None:
        super().__init__(dataset_as_path)

    def predict(self, data: YearInWeeks) -> SimpleClassifiedYear:
        """
        Classify every week as related or not to the life event
        :param data: the YearInWeeks, containing data aggregated by Tapoi
        :return: a SimpleClassifiedYear, which is a set of boolean labels for each week of the year
        """
        classified_year: SimpleClassifiedYear = SimpleClassifiedYear()
        for week in data.get_all_weeks():
            # check that the week contains at least one entity of the classifier
            at_least_one = False
            uris = [d for d in data.get_week(week)]
            for u in uris:
                if u in self._indexes:
                    at_least_one = True
            # in case at least one entity is found, go for classification
            # otherwise false
            if at_least_one:
                X = np.zeros((1, len(self._indexes)))
                for uri in data.get_week(week):
                    if uri in self._indexes:
                        print(uri)
                        X[0][self._indexes[uri]] += 1
                classified_year.with_week(week, self.tree.predict(X)[0])
            else:
                classified_year.with_week(week, False)
        return classified_year


class SimpleWeddingDecisionTree(SimpleDecisionTree):
    """
    Simple decision tree for marriage
    """

    DATASET = "getting_married.json"

    def __init__(self) -> None:
        super().__init__(SimpleWeddingDecisionTree.DATASET)


class SimpleBirthDecisionTree(SimpleDecisionTree):
    """
    Simple decision tree for marriage
    """

    DATASET = "having_children.json"

    def __init__(self) -> None:
        super().__init__(SimpleBirthDecisionTree.DATASET)