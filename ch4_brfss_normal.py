import sys
import brfss
import math
import ch4_rankit as rankit


def main(data_dir):
    resp = brfss.Respondents()
    resp.ReadRecords(data_dir)
    w = [r.weight2 for r in resp.records if r.weight2 != 'NA']
    logw = map(math.log, w)
    rankit.makeNormalPlot(logw)


if __name__ == '__main__':
    main(sys.argv[1])
