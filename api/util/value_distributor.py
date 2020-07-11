from collections import namedtuple
from random import choice

ValueCount = namedtuple("ValueCount", ["value", "count"])


class WeightedValue(object):
    """Stores a count of weighted values.
    """

    def __init__(self, value, count, weight):
        """Set value, count, and weight.

        Params:
            value Any The value to generate a weighted count for.
            count int The count for this value.
            weight int The weight for this value.
        """
        self.value = value
        self.count = count
        self.weight = weight

    def increment(self, max):
        """Increment the count by 1.

        Params:
            max int The max count after increment.

        Return:
            True if the count can be incremented again.
        """
        self.count += 1
        return self.count < max

    def __str__(self):
        return "WeightedValue(value={0}, count={1}, weight={2})".format(
            self.value, self.count, self.weight
        )


class ValueDistributor(object):
    """Distribute counts over a list of values.
    """

    def __init__(self, minCountPer=1, maxCountPer=10):
        """Set minimum count per, and values.
        Values arg is there to support deepcopy.

        Params:
            minCountPer int The count to start each value with [default 1]
            maxCountPer int The max count per value [default 10]
        """
        self.values = list()
        self.minCountPer = minCountPer
        self.maxCountPer = 10

    def add(self, value, weight=1, minCount=None):
        """Add a value to the distributor.

        Params:
            value Any value to count (usually a string).
            weight int weight of the value.
            minCount int overrides the minCountPer.
        """
        self.values.append(
            WeightedValue(
                value=value,
                count=self.minCountPer if not minCount else minCount,
                weight=weight,
            )
        )

    def roll(self, numRolls=None, **args):
        """Execute a number of roll operations to increment counts.

        Params:
            numRolls int The number of increments to make.
            totalRolls int The target count total.
        """
        totalRolls = args.get("totalRolls", None)

        if totalRolls:
            numRolls = totalRolls - self._totalCount()

        workingSkillList = [v for v in self.values]
        for i in range(0, numRolls):
            if not workingSkillList:
                return
            skill = choice(workingSkillList)
            if not skill.increment(self.maxCountPer):
                workingSkillList.remove(skill)

    def getValueCounts(self):
        """Returns a list of ValueCount namedtuples (value=, count=).
        """
        return [
            ValueCount(value=v.value, count=v.count)
            for v in self.values
            if v.count > 0
        ]

    def getSkillNames(self):
        return [s.value for s in self.values]

    def _getWeights(self):
        return [v.weight for v in self.values]

    def _totalCount(self):
        return sum([v.count for v in self.values])

    def __str__(self):
        return "\n".join(
            ["ValueDistributor"] + ["\t" + str(v) for v in self.values]
        )
