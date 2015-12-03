"""
risk.py implementation
"""

import sys
import survey
import ch1
import Pmf


def probPMF(pmf, start, end):
    total = 0.0
    for val, prob in pmf.Items():
        if val > end:
            break
        elif val >= start:
            total += prob
    return total


def probEarly(pmf):
    return probPMF(pmf, 0, 37)


def probOnTime(pmf):
    return probPMF(pmf, 38, 40)


def probLate(pmf):
    return probPMF(pmf, 41, 50)


def ComputeRelativeRisk(first_pmf, other_pmf):
    """Computes relative risks for two PMFs.

    first_pmf: Pmf object
    other_pmf: Pmf object
    """
    print 'Risks:'
    funcs = [probEarly, probOnTime, probLate]
    risks = {}
    for func in funcs:
        for pmf in [first_pmf, other_pmf]:
            prob = func(pmf)
            risks[func.__name__, pmf.name] = prob
            print func.__name__, pmf.name, prob

    print
    print 'Risk ratios (first babies / others):'
    for func in funcs:
        try:
            ratio = (risks[func.__name__, 'first babies'] /
                     risks[func.__name__, 'others'])
            print func.__name__, ratio
        except ZeroDivisionError:
            pass


if __name__ == '__main__':
    table = survey.Pregnancies()
    table.ReadRecords(sys.argv[1])
    first, other = ch1.partition_births(table)
    pmf_first = Pmf.MakePmfFromList((rec.prglength for rec in first.records),
                                    'first babies')
    pmf_other = Pmf.MakePmfFromList((rec.prglength for rec in other.records),
                                    'others')
    ComputeRelativeRisk(pmf_first, pmf_other)
