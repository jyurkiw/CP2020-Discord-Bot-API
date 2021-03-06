import pytest
from unittest import TestCase

from ...stats.stat import Stat


class TestStatGeneration(TestCase):
    def setUp(self):
        self.statIds = [
            (0, "INT"),
            (1, "REF"),
            (2, "TECH"),
            (3, "COOL"),
            (4, "ATTR"),
            (5, "LUCK"),
            (6, "MA"),
            (7, "BODY"),
            (8, "EMP"),
        ]

        self.testStatName = "TEST"
        self.testStatMin = 3
        self.testStatMax = 5
        self.testStat = Stat(self.testStatName, self.testStatMin)

    def test_stat_minStatGetsSet(self):
        self.assertEqual(self.testStat.value, self.testStatMin)

    def test_stat_statNameGetsSet(self):
        self.assertEqual(self.testStat.name, self.testStatName)

    def test_stat_incrementIncreasesStatByOne(self):
        self.testStat.increment(self.testStatMax)
        self.assertEqual(self.testStat.value, 4)

    def test_stat_incrementCanIncreaseStatToMax(self):
        self.testStat.increment(self.testStatMax)
        self.testStat.increment(self.testStatMax)
        self.assertEqual(self.testStat.value, self.testStatMax)

    def test_stat_incrementCanNotIncreaseStatPastMax(self):
        self.testStat.increment(self.testStatMax)
        self.testStat.increment(self.testStatMax)
        self.testStat.increment(self.testStatMax)
        self.assertEqual(self.testStat.value, self.testStatMax)

    def test_stat_incrementSuccessReturnsTrue(self):
        result = self.testStat.increment(self.testStatMax)
        self.assertTrue(result)

    def test_stat_incrementPastMaxReturnsFalse(self):
        self.testStat.increment(self.testStatMax)
        self.testStat.increment(self.testStatMax)
        result = self.testStat.increment(self.testStatMax)
        self.assertFalse(result)
