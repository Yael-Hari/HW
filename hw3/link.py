from data import Data
from sample import Sample


class Link:
    def __init__(self):
        self.data = Data('Leukemia_sample.csv')
        self.samples_list = self.data.create_samples()

    def compute(self, cluster, other, distances_matrix):
        pass


class SingleLink(Link):
    """
    compute the distance between the two closest points in clusters.
    """
    def __init__(self):
        super().__init__()

    def compute(self, cluster, other, distances_matrix):
        distances = []
        for sample_i in cluster.samples:
            for sample_j in other.samples:
                distances.append(distances_matrix[sample_i.s_id][sample_j.s_id])
        return min(distances)


class CompleteLink(Link):
    def __init__(self):
        super().__init__()

    def compute(self, cluster, other, distances_matrix):
        distances = []
        for sample_i in cluster.samples:
            for sample_j in other.samples:
                distances.append(distances_matrix[sample_i.s_id][sample_j.s_id])
        return max(distances)


methods_list = [SingleLink, CompleteLink]