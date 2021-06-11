from cluster import Cluster
from link import method


class AgglomerativeClustering:
    def __init__(self, link, samples):
        self.link = link
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
           for point in cluster:
               find_min_out = []
               for other in self.clusters:
                   if cluster != other:
                       find_min_out.append(other.distance_to_point(point, False))
               outxi = (min(find_min_out))
               inxi = (cluster.distance_to_point(point, True))
               dict_sh[point.s_id] = 0
               if (len(cluster.samples > 1)):
                   dict_sh[point.s_id] = (outxi - inxi)/max(inxi, outxi)
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
            dict_summery[cluster.c_id] = cluster_sil/len(cluster.samples)
        dict_summery[0] = all_sil/points_counter
        return dict_summery

    #def compute_rand_index(self):

    def run(self, number_of_clusters):
        for i in range (0,2):
             meth = method[i]()
             dis = meth.compute(self.clusters[0], self.clusters[1])
             while len(self.clusters) > number_of_clusters:
                most_close = [0, 0]
                for cluster in self.clusters:
                    for other in self.clusters:
                        if cluster != other:
                            new_dis = meth.compute(cluster, other)
                            if new_dis < dis:
                                dis = new_dis
                                most_close[0] = cluster
                                most_close[1] = other
                most_close[0].merge(most_close[1])
        print ('single link')
        for i in self.clusters:
            print('Cluster ', i.c_id,': ',i.samples.s_id)






























