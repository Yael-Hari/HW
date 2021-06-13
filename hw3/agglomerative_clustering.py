from cluster import Cluster
from link import method


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
        self.samples = samples
        self.clusters = []
        cluster_index = 0
        for sample in samples:
            one_sample_list = [sample]
            cluster = Cluster(cluster_index, one_sample_list)
            self.clusters.append(cluster)
            cluster_index += 1

    def compute_silhoeutte(self):
        dict_sh = {}
        for cluster in self.clusters:
            for point in cluster.samples:
                find_min_out = []
                for other in self.clusters:
                    if cluster != other:
                        find_min_out.append(other.distance_to_point(point, False))
                out_xi = (min(find_min_out))
                in_xi = (cluster.distance_to_point(point, True))
                dict_sh[point.s_id] = 0
                if len(cluster.samples > 1):
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
            for sample in cluster:
                cluster_sil += dict_sh[sample.s_id]
            all_sil += cluster_sil
            dict_summery[cluster.c_id] = cluster_sil / len(cluster.samples)
        dict_summery[0] = all_sil / points_counter
        return dict_summery

    def compute_rand_index(self):
        total_count, correct_count = 0, 0
        for i in self.samples:
            for j in self.samples[i:]:
                cluster_i = [cluster.c_id for cluster in self.clusters if i in cluster.samples][0]  # todo works??
                cluster_j = [cluster.c_id for cluster in self.clusters if j in cluster.samples][
                    0]  # only 1 item in these lists
                if (cluster_i == cluster_j) == (i.label == j.label):
                    correct_count += 1
                total_count += 1
        return correct_count / total_count

    def run(self, number_of_clusters):
        for i in range(0, 2):
            meth = method[i]()
            dis = meth.compute(self.clusters[0], self.clusters[1])
            while len(self.clusters) > number_of_clusters:
                merge_index = len(self.clusters) + 1
                other_index = len(self.clusters) + 1
                for k in range(len(self.clusters)):
                    for j in range(len(self.clusters)):
                        if k != j:
                            new_dis = meth.compute(self.clusters[k], self.clusters[j])
                            if new_dis < dis:
                                dis = new_dis
                                merge_index = k
                                other_index = j
                if merge_index != len(self.clusters) + 1:
                    self.clusters[merge_index].merge(self.clusters[other_index])

        print("single link")

        for i in self.clusters:
            print("Cluster " + i.c_id + " :" + i.samples.s_id)
