import ch4_rankit as rankit
import relay


if __name__ == '__main__':
    results = relay.ReadResults()
    speeds = relay.GetSpeeds(results)
    rankit.makeNormalPlot(speeds)
