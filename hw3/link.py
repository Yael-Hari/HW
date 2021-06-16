from data import Data
from sample import Sample


class Link:
    def compute(self, cluster, other, distances_matrix):
        pass


class SingleLink(Link):
    def compute(self, cluster, other, distances_matrix):
        """
        compute the distance between the two closest points in clusters.
        """
        distances = []
        for sample_i in cluster.samples:
            for sample_j in other.samples:
                distances.append(distances_matrix[sample_i.s_id][sample_j.s_id])
        return min(distances)


class CompleteLink(Link):
    def compute(self, cluster, other, distances_matrix):
        """
        compute the distance between the two furthest points in clusters.
        """
        distances = []
        for sample_i in cluster.samples:
            for sample_j in other.samples:
                distances.append(distances_matrix[sample_i.s_id][sample_j.s_id])
        return max(distances)


methods_list = [SingleLink, CompleteLink]