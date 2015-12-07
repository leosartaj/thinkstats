import numpy as np
import random
import matplotlib.pyplot as plt


def Sample(n=6, mu=0, sigma=1):
    return sorted([random.normalvariate(mu, sigma) for i in range(n)])


def Samples(m=1000, n=6, mu=0, sigma=1):
    return [Sample(n, mu, sigma) for i in range(m)]


def estimateRankit(m=1000, n=6):
    return [np.array(l).mean() for l in zip(*Samples(m, n))]


def makeNormalPlot(y):
    x = Sample(len(y))
    plt.plot(sorted(x), sorted(y), 'b.', markersize=3)
    plt.show()


if __name__ == '__main__':
    print estimateRankit()
