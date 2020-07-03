import pytest
from unittest import TestCase

from ...stats.statblock import StatBlock


class TestStatBlockGenerationDefaults(TestCase):
    def setUp(self):
        self.testStatBlock = StatBlock()

    def test_statBlock_minStatIs2(self):
        self.assertEqual(self.testStatBlock.minStat, 2)

    def test_statBlock_maxStatIs10(self):
        self.assertEqual(self.testStatBlock.maxStat, 10)

    def test_statBlock_minTotalIsNone(self):
        self.assertEqual(self.testStatBlock.minTotal, None)

    def test_statBlock_maxTotalIsNone(self):
        self.assertEqual(self.testStatBlock.maxTotal, None)

    def test_statBlock_totalStatsIsNone(self):
        self.assertEqual(self.testStatBlock.totalStats, None)

    def test_statBlock_statTotalIs18(self):
        self.assertEqual(self.testStatBlock.getStatTotal(), 18)


class TestGenerateRandom(TestCase):
    def setUp(self):
        pass

    def test_generateRandom_bruteForce1k_noArgs(self):
        for statblock_id in range(1, 1000):
            statBlock = StatBlock().generateRandom()
            for value in statBlock.toSimpleList():
                self.assertGreaterEqual(value, 2)
                self.assertLessEqual(value, 10)

    def test_generateRandom_bruteForce1k_totalStats(self):
        for statblock_id in range(1, 1000):
            statBlock = StatBlock(totalStats=90).generateRandom()
            for value in statBlock.toSimpleList():
                self.assertEqual(value, 10)

    def test_generateRandom_bruteForce1k_minStats(self):
        for statBlock_id in range(1, 1000):
            statBlock = StatBlock(minTotal=79)
            statBlock._generateRandom_setDefaultTotals()

            self.assertGreaterEqual(statBlock.totalStats, 79)
            self.assertLessEqual(statBlock.totalStats, 80)
