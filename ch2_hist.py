"""
Chapter 2
"""

import operator, sys
import matplotlib.pyplot as plt
import seaborn as sns
import survey
import ch1


def Mode(hist):
    return hist.MaxLike


def AllModes(hist):
    return sorted(hist.Items(), key=operator.itemgetter(1), reverse=True)


def draw_hist(d):
    table = survey.Pregnancies()
    table.ReadRecords(d)
    first, other = ch1.partition_births(table)
    first_preg = [rec.prglength for rec in first.records]
    other_preg = [rec.prglength for rec in other.records]
    l1 = sns.distplot(first_preg, kde=False)
    l2 = sns.distplot(other_preg, kde=False)
    plt.legend(['first', 'other'], loc=2)
    plt.show()


if __name__ == '__main__':
    draw_hist(sys.argv[1])
