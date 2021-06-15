from cluster import Cluster
from link import *


class AgglomerativeClustering:
    def __init__(self, link, samples, distances_matrix):
        self.link = link
        self.samples = samples
        self.distances_matrix = distances_matrix
        self.clusters = []

        # every point gets a cluster
        cluster_index = 0
        for sample in samples:
            one_sample_list = [sample]
            cluster = Cluster(sample.s_id, one_sample_list)
            self.clusters.append(cluster)
            cluster_index += 1

    def compute_silhoeutte(self):
        dict_sh = {}
        for cluster in self.clusters:
            for point in cluster.samples:
                find_min_out = []
                for other in self.clusters:
                    if cluster != other:
                        find_min_out.append(other.distance_to_point(point, False, self.distances_matrix))
                out_xi = (min(find_min_out))
                in_xi = (cluster.distance_to_point(point, True, self.distances_matrix))
                dict_sh[point.s_id] = 0
                if len(cluster.samples) > 1:
                    dict_sh[point.s_id] = (out_xi - in_xi) / max(in_xi, out_xi)
        return dict_sh

    def compute_summery_silhoeutte(self):
        points_counter = 0
        all_sil = 0
        dict_summery = {}
        dict_sh = self.compute_silhoeutte()
        for cluster in self.clusters:
            points_counter += len(cluster.samples)
            cluster_sil = 0
            for sample in cluster.samples:
                cluster_sil += dict_sh[sample.s_id]
            all_sil += cluster_sil
            dict_summery[cluster.c_id] = cluster_sil / len(cluster.samples)
        dict_summery[0] = all_sil / points_counter
        return dict_summery

    def compute_rand_index(self):
        total_count, correct_count = 0, 0
        for index, i in enumerate(self.samples):
            for j in self.samples[index+1:]:
                cluster_i = [cluster.c_id for cluster in self.clusters if i in cluster.samples][0]
                cluster_j = [cluster.c_id for cluster in self.clusters if j in cluster.samples][0]  # only 1 item in these lists
                if (cluster_i == cluster_j) == (i.lable == j.lable):
                    correct_count += 1
                total_count += 1
        return correct_count / total_count

    def run(self, max_clusters):
        while len(self.clusters) > max_clusters:
            cluster1_index = 0
            cluster2_index = 1
            distance = self.link.compute(self.clusters[0], self.clusters[1], self.distances_matrix)
            for i in range(len(self.clusters)):
                for j in range(i+1, len(self.clusters)):
                    new_distance = self.link.compute(self.clusters[i], self.clusters[j], self.distances_matrix)

                    if new_distance < distance:
                        distance = new_distance
                        cluster1_index = i
                        cluster2_index = j

            self.clusters[cluster1_index].merge(self.clusters[cluster2_index])
            del self.clusters[cluster2_index]

        # print results
        silhouette_dict = self.compute_summery_silhoeutte()
        for cluster in self.clusters:
            cluster.print_details(silhouette=silhouette_dict[cluster.c_id])
        print("Whole data: silhouette =", round(silhouette_dict[0], 3), end="")
        print(", RI =", round(self.compute_rand_index(), 3), end="\n\n")






