import sys
import numpy as np
import erf
import survey
import Cdf
import myplot


def live_births(table):
    new_table = survey.Pregnancies()
    for rec in table.records:
        if rec.outcome == 1:
            new_table.AddRecord(rec)
    return new_table


def mean_std(table):
    arr = np.array([rec.prglength for rec in table.records])
    return arr.mean(), arr.std()


def main(filename):
    table = survey.Pregnancies()
    table.ReadRecords(filename)
    table = live_births(table)
    cdf = Cdf.MakeCdfFromList([rec.prglength for rec in table.records])
    myplot.Cdf(cdf)
    myplot.Show()
    _, std = mean_std(table)
    myplot.Cdf(erf.MakeNormalCdf(-3*std, 3*std))
    myplot.Show()


if __name__ == '__main__':
    main(sys.argv[1])
