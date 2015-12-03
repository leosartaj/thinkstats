"""
Conditional Probability
"""
import sys
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np
import survey
import Pmf
import ch1


def cond_born(pmf, on):
    for i in range(on):
        try:
            pmf.Remove(i)
        except KeyError:
            pass
    pmf.Normalize()
    return pmf.Prob(on)


def draw_hist(d):
    table = survey.Pregnancies()
    table.ReadRecords(d)
    first, other = ch1.partition_births(table)
    first_preg = np.array([rec.prglength for rec in first.records])
    other_preg = np.array([rec.prglength for rec in other.records])
    pmf_first = Pmf.MakePmfFromList(first_preg)
    pmf_other = Pmf.MakePmfFromList(other_preg)
    x = [i for i in range(34, 47)]
    y1 = [cond_born(pmf_first, i) for i in range(34, 47)]
    y2 = [cond_born(pmf_other, i) for i in range(34, 47)]
    l1 = plt.plot(x, y1)
    l2 = plt.plot(x, y2)
    plt.legend(['first', 'other'], loc=2)
    plt.show()


if __name__ == '__main__':
    sns.set_style("darkgrid")
    draw_hist(sys.argv[1])
