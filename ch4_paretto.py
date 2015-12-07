import random
import matplotlib.pyplot as plt
import myplot
import Cdf


def paretovariate(alpha, xm):
    return xm * random.paretovariate(alpha)


def main():
    p = [paretovariate(1, 0.5) for i in range(100)]
    cdf = Cdf.MakeCdfFromList(p)
    myplot.Cdf(cdf, transform='pareto')
    myplot.Show()


if __name__ == '__main__':
    main()
