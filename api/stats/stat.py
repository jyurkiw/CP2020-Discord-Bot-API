from random import randint

INT = "INT"
REF = "REF"
TECH = "TECH"
COOL = "COOL"
ATTR = "ATTR"
LUCK = "LUCK"
MA = "MA"
BODY = "BODY"
EMP = "EMP"


STATS = [INT, REF, TECH, COOL, ATTR, LUCK, MA, BODY, EMP]


def get_min_stats(minStat):
    return [Stat(name, minStat) for name in STATS]


class Stat(object):
    def __init__(self, name, minStat):
        self.value = minStat
        self.name = name

    def increment(self, max):
        if self.value < max:
            self.value += 1
        return not self.isMax(max)

    def setRandom(self, min=2, max=10):
        self.value = randint(min, max)

    def isMax(self, max):
        return self.value >= max

    def validIncrement(self, max):
        return self.value < max
