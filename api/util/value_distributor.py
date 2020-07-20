from random import choice


def getTotal(values, countGetter):
    return sum([countGetter(v) for v in values])


def distributeValues(
    values,
    keyGetter=None,
    countGetter=None,
    incrementor=None,
    points=40,
    total=80,
    max=10,
):
    """Distribute counts randomly between their starting value and max over a
    list of values.
    """
    if not keyGetter:
        raise Exception("keyGetter is required. Found None")
    if not countGetter:
        raise Exception("countGetter is required. Found None")
    if not incrementor:
        raise Exception("incrementor is required. Found None")

    vDict = {keyGetter(v): v for v in values}
    _total = getTotal(values, countGetter) + points
    total = min(total, _total)

    while getTotal(values, countGetter) < total and vDict:
        c = vDict[choice([k for k in vDict.keys()])]
        incrementor(c)
        if countGetter(c) >= max:
            print("removing " + str(keyGetter(c)))
            del vDict[keyGetter(c)]
