from sample import Sample
from data import Data


class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id         #cluster's id
        self.samples = samples  #list of samples

    def merge(self, other):
        merged = self.samples + other.samples
        merged.sort(key=lambda x: x.s_id)
        self.c_id = min(self.c_id, other.c_id)
        self.samples = merged
        del other

    def distance_to_point(self, point, incluster):
        distance = 0
        for other in self.samples:
            sum = 0
            if point != other:
                for j in range(len(other.genes)):
                    sum += (point.genes[j] - other.genes[j])**2
            sum = sum**0.5
            if incluster:
                distance += (1/(len(self.samples)-1)) * sum
            else:
                distance += (1 / len(self.samples)) * sum
        return

    #def print_details(self, silhouette):




