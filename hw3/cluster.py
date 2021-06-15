from sample import Sample
from data import Data


class Cluster:
    def __init__(self, c_id, samples):
        self.c_id = c_id        #cluster's id
        self.samples = samples  #list of samples

    def merge(self, other):
        # print("merge")
        merged = self.samples + other.samples
        merged.sort(key=lambda x: x.s_id)
        self.c_id = min(self.c_id, other.c_id)
        self.samples = merged

    def distance_to_point(self, point, incluster, distances_matrix):
        distance = 0
        for other in self.samples:
            distance_to_point = distances_matrix[point.s_id][other.s_id]
            if incluster:
                if len(self.samples) == 1:
                    return 0
                distance += (1/(len(self.samples)-1)) * distance_to_point
            else:
                distance += (1 / len(self.samples)) * distance_to_point
        return distance

    def find_dominant_lable(self, samples):
        dict = {}
        for i in range(len(samples)):
            if samples[i].lable not in dict.keys():
                dict[samples[i].lable] = 0;
            dict[samples[i].lable] += 1
        max_value = max(dict.values())
        return [k for k, v in dict.items() if v == max_value][0]

    def print_details(self, silhouette):
        list_of_samples_id = [sample.s_id for sample in self.samples]
        print("Cluster", str(self.c_id) + ":", list_of_samples_id, end="")
        print(", dominant label =", self.find_dominant_lable(self.samples), end="")
        print(", silhouette =", round(silhouette, 3))





