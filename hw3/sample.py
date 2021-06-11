from math import sqrt


class Sample:
    def __init__(self, s_id, genes, lable):
        self.s_id = s_id
        self.genes = genes  # list
        self.lable = lable  # type

    def compute_euclidean_distance(self, other):
        sum = 0
        for i in range(len(self.genes)):
            sum += (self.genes[i] - other.genes[i])**2
        return sqrt(sum)

    @staticmethod
    def compute_distances_matrix(samples_list):
        distances_matrix = [[0 for x in range(0, 282)] for y in range(0, 282)]

        for sample in samples_list:
            for other in samples_list:
                distances_matrix[sample.s_id][other.s_id] = sample.compute_euclidean_distance(other)

        return distances_matrix