"""
Chapter 1
"""

import sys
import survey
import thinkstats as ts

def live_births(table):
    cou = 0
    for rec in table.records:
        if rec.outcome == 1:
            cou += 1
    return cou


def partition_births(table):
    first = survey.Pregnancies()
    other = survey.Pregnancies()

    for rec in table.records:
        if rec.outcome != 1:
            continue
        if rec.birthord == 1:
            first.AddRecord(rec)
        else:
            other.AddRecord(rec)
    return first, other


def average(table):
    return (sum(rec.prglength for rec in table.records) /
            float(len(table.records)))


def MeanVar(table):
    return ts.MeanVar([rec.prglength for rec in table.records])


def summarize(table):
    """Prints summary statistics for first babies and others.

    Returns:
        tuple of Tables
    """
    first, other = partition_births(table)

    print 'Number of first babies', len(first.records)
    print 'Number of others', len(other.records)

    (mu1, st1), (mu2, st2) = MeanVar(first), MeanVar(other)

    print 'Mean gestation in weeks:'
    print 'First babies', mu1
    print 'Others', mu2
    print 'Difference in days', (mu1 - mu2) * 7.0

    print 'STD of gestation in weeks:'
    print 'First babies', st1
    print 'Others', st2
    print 'Difference in days', (st1 - st2) * 7.0



if __name__ == '__main__':
    table = survey.Pregnancies()
    table.ReadRecords(sys.argv[1])
    summarize(table)
