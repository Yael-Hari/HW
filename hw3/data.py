import pandas as pd
from sample import Sample


class Data:
    def __init__(self, path):
        df = pd.read_csv(path)
        self.data = df.to_dict(orient="list")

    def create_samples(self):
        """
        :return: a list of samples
        """
        sample_list = []
        key_list = self.data.keys()
        for i in range(len(self.data['samples'])):
            gene_list = []
            for j in key_list:
                if j != 'samples' and j != 'type':
                    gene_list.append(self.data[j][i])
            sample = Sample(self.data['samples'][i], gene_list, self.data['type'][i])
            sample_list.append(sample)
        return sample_list


