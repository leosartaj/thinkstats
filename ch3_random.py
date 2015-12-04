import random
import Cdf
import Pmf
import myplot


if __name__ == '__main__':
    l = [random.random() for i in range(100000)]
    cdf = Cdf.MakeCdfFromList(l)
    pmf = Pmf.MakePmfFromList(l)
    myplot.Cdf(cdf)
    myplot.Pmf(pmf)
    myplot.Show()
