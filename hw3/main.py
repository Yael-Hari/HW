import sys
from data import Data
from sample import Sample
from agglomerative_clustering import AgglomerativeClustering
from link import *


def main(argv):
    data = Data(argv[1])
    sample_list = data.create_samples()
    header_link = ["single link:", "complete link:"]
    for i, method in enumerate(methods_list):
        print(header_link[i])
        link = method()
        m = AgglomerativeClustering(link, sample_list)
        m.run(7)


if __name__ == '__main__':
    main(sys.argv)