class Link:
    def __init__(self):
        pass

    def compute(self, cluster, other):
        pass


class SingleLink(Link):
    """
    compute thd distance between the two closest points in clusters.
    """
    def compute(self, cluster, other):
        distances_matrix = []

        for i, sample_i in enumerate(cluster.samples):
            for j, sample_j in enumerate(other.samples):
                distances_matrix[i][j] = sample_i.compute_euclidean_distance(sample_j)

        return min([min(x) for x in distances_matrix])


class CompleteLink(Link):
    def compute(self, cluster, other):
        distances_matrix = []

        for i, sample_i in enumerate(cluster.samples):
            for j, sample_j in enumerate(other.samples):
                distances_matrix[i][j] = sample_i.compute_euclidean_distance(sample_j)

        return max([max(x) for x in distances_matrix])


method = [SingleLink, CompleteLink]