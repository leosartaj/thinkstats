import random, math
import matplotlib.pyplot as plt
import myplot
import Cdf


def weibullvariate(lam, k):
    p = random.random()
    return lam * (-math.log(1 - p))**(1/k)


def main():
    p = [weibullvariate(1, 0.5) for i in range(1000)]
    cdf = Cdf.MakeCdfFromList(p)
    myplot.Cdf(cdf, transform='weibull')
    myplot.Show()


if __name__ == '__main__':
    main()
