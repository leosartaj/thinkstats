def percentile(scores, percentile_rank):
    idx = ((len(scores) - 1) * percentile_rank) / 100
    return sorted(scores)[idx]


print percentile([55, 66, 77, 88, 99], 50)
