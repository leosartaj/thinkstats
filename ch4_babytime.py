"""
Plots interarrival time of babies
"""
import sys
import Cdf
import myplot
import random


def get_times(filename):
    """Get all the times in minutes"""
    with open(filename) as f:
        r, times = 0, []
        for line in f:
            if r:
                times.append(line.split()[0])
            if line == 'START DATA:\n':
                r = 1
    return times


def time_in_minutes(times):
    for idx, time in enumerate(times):
        times[idx] = int(time[:2]) * 60 + int(time[2:])
    return times


def interarrival(times):
    l = len(times)
    for idx, time in enumerate(times[::-1]):
        times[l - idx - 1] = time - times[l - idx - 2]
    times[0] = 0
    return times


def main(filename):
    times = get_times(filename)
    times = time_in_minutes(times)
    times = interarrival(times)
    cdf = Cdf.MakeCdfFromList(times)
    myplot.Cdf(cdf, complement=True, xscale='linear', yscale='log')
    myplot.Show()
    new_cdf = Cdf.MakeCdfFromList([random.expovariate(1/32.6) for i in range(44)])
    myplot.Cdf(new_cdf, complement=True, xscale='linear', yscale='log')
    myplot.Show()


if __name__ == '__main__':
    main(sys.argv[1])
