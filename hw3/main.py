import sys
from data import Data
from sample import Sample
from agglomerative_clustering import AgglomerativeClustering
from link import SingleLink


def main(argv):
    data = Data('Leukemia_sample.csv')
    sample_list = data.create_samples()
    link = SingleLink()
    m = AgglomerativeClustering(link, sample_list)
    m.run(7)


if __name__ == '__main__':
    main(sys.argv)