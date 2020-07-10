from collections import namedtuple
from random import choices

import copy

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

    def increment(self):
        """Increment the count by 1.
        """
        self.count += 1

    def __deepcopy__(self, memo=None):
        return WeightedValue(self.value, self.count, self.weight)

    def __str__(self):
        return "WeightedValue(value={0}, count={1}, weight={2})".format(
            self.value, self.count, self.weight
        )


class ValueDistributor(object):
    """Distribute counts over a list of values.
    """

    def __init__(self, minCountPer=1, values=[]):
        """Set minimum count per, and values.
        Values arg is there to support deepcopy.

        Params:
            minCountPer int The count to start each value with [default 1]
        """
        self.values = values
        self.minCountPer = minCountPer

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

        Return:
            A list of ValueCount namedtuples (name=, value=)
        """
        totalRolls = args.get("totalRolls", None)

        if totalRolls:
            numRolls = totalRolls - self._totalCount()

        for v in choices(self.values, self._getWeights(), k=numRolls):
            v.increment()

        return self._calculateReturnList()

    def _getWeights(self):
        return [v.weight for v in self.values]

    def _totalCount(self):
        return sum([v.count for v in self.values])

    def _calculateReturnList(self):
        return [
            ValueCount(value=v.value, count=v.count)
            for v in self.values
            if v.count > 0
        ]

    def __deepcopy__(self, memo=None):
        return ValueDistributor(
            self.minCountPer, [copy.deepcopy(v) for v in self.values]
        )

    def clone(self):
        """Returns a deepcopy of this object.
        Useful for a factory pattern.
        """
        return copy.deepcopy(self)

    def __str__(self):
        return "\n".join(
            ["ValueDistributor"] + ["\t" + str(v) for v in self.values]
        )
