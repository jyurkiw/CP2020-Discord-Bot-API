from random import randint, choice
from .stat import get_min_stats

MIN_STAT = "minStat"
MAX_STAT = "maxStat"
MIN_TOTAL = "minTotal"
MAX_TOTAL = "maxTotal"
TOTAL_STATS = "totalStats"


class StatBlock(object):
    def __init__(self, **varargs):
        self.minStat = varargs.get(MIN_STAT, 2)
        self.maxStat = varargs.get(MAX_STAT, 10)
        self.minTotal = varargs.get(MIN_TOTAL, None)
        self.maxTotal = varargs.get(MAX_TOTAL, None)
        self.totalStats = varargs.get(TOTAL_STATS, None)
        self.stats = get_min_stats(self.minStat)

    def generateRandom(self):
        if self.minTotal or self.maxTotal:
            self._generateRandom_setDefaultTotals()

        if self.totalStats is not None:
            self._generateRandom_incrementalBuildByTotal()
        else:
            self._generateRandom_setRandomStatValues()

        return self

    def _generateRandom_setDefaultTotals(self):
        self.minTotal = self.minTotal if self.minTotal else 40
        self.maxTotal = self.maxTotal if self.maxTotal else 80
        self.totalStats = randint(self.minTotal, self.maxTotal)

    def _generateRandom_incrementalBuildByTotal(self):
        statLen = len(self.stats)
        while self.getStatTotal() < self.totalStats:
            validStats = [
                idx
                for idx in range(0, statLen)
                if self.stats[idx].validIncrement(self.maxStat)
            ]
            if not validStats:
                return

            self.stats[choice(validStats)].increment(self.maxStat)

    def _generateRandom_setRandomStatValues(self):
        for stat in self.stats:
            stat.setRandom(self.minStat, self.maxStat)

    def toSimpleList(self):
        """
        Return a simple list of all stat values.
        """
        return [stat.value for stat in self.stats]

    def getStatTotal(self):
        """
        Get the total of all stat values in the block.
        """
        return sum(self.toSimpleList())
