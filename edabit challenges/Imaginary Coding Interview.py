def interview(lst, tot):
    if len(lst) < 8 or tot > 120:
        return "disqualified"

    time_limits = [5, 5, 10, 10, 15, 15, 20, 20]

    for i, time_limit in enumerate(time_limits):
        if lst[i] > time_limit:
            return "disqualified"

    if sum(lst) > tot:
        return "disqualified"

    return "qualified"

