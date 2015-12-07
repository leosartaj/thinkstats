import sys
import populations
import Cdf
import myplot


def main(filename):
    pops = populations.ReadData(filename)
    cdf = Cdf.MakeCdfFromList(pops)
    myplot.Cdf(cdf, transform='pareto')
    myplot.Show()


if __name__ == '__main__':
    main(sys.argv[1])
