"""
Class Size Paradox
"""

import Pmf


def FactorPmf(pmf, factor):
    new_pmf = pmf.Copy()

    for x, p in pmf.Items():
        new_pmf.Mult(x, factor(x))

    new_pmf.Normalize()
    return new_pmf


if __name__ == '__main__':
    pmf = Pmf.MakePmfFromDict({7: 8, 12: 8, 17: 14, 22: 4, 27: 6, 32: 12,
                               37: 8, 42: 3, 47: 2})

    print 'Actual'
    print 'Mean ->', pmf.Mean()
    print 'Var ->', pmf.Var()

    obs_pmf = FactorPmf(pmf, lambda x: x)
    print 'Observed'
    print 'Mean ->', obs_pmf.Mean()
    print 'Var ->', obs_pmf.Var()

    unb_pmf = FactorPmf(obs_pmf, lambda x: 1.0 / x)
    print 'Unbiased'
    print 'Mean ->', unb_pmf.Mean()
    print 'Var ->', unb_pmf.Var()
