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