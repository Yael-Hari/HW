import sys
from data import Data
from sample import Sample
from agglomerative_clustering import AgglomerativeClustering
from link import *


def main(argv):
    data = Data(argv[1])
    sample_list = data.create_samples()
    header_link = ["single link:", "complete link:"]

    distances_matrix = compute_distances_matrix(sample_list)

    for i, method in enumerate(methods_list):
        print(header_link[i])
        link = method()
        m = AgglomerativeClustering(link, sample_list, distances_matrix)
        m.run(7)


def compute_distances_matrix(samples_list):
    distances_matrix = [[0 for x in range(0, 282)] for y in range(0, 282)]

    for sample in samples_list:
        for other in samples_list:
            distances_matrix[sample.s_id][other.s_id] = sample.compute_euclidean_distance(other)

    return distances_matrix


if __name__ == '__main__':
    main(sys.argv)