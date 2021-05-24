import sys
from data import Data
from sample import Sample


def main(argv):
    samps = []
    for i in range(5):
        samps.append(Sample(i, [i, i+8], 'hello '+str(i)))
    my_samp = Sample(1, [1, 9], 'hello 1')
    print(my_samp in samps)


if __name__ == '__main__':
    main(sys.argv)