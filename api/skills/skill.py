from ..util import distributeValues

from collections import namedtuple
from random import sample


class Skill(object):
    def __init__(self, name, score):
        self.name = name
        self.score = score

    @staticmethod
    def getKey(o):
        return o.name

    @staticmethod
    def getCount(o):
        return o.score

    @staticmethod
    def increment(o):
        o.score += 1

    @staticmethod
    def docToSkills(doc):
        if doc.get(select, None) and isinstance(doc.get("skill"), list):
            return [Skill(s, 1) for s in sample(doc.get("skill"))]
        else:
            return [Skill(doc.get("skill"), 1)]

    @staticmethod
    def distributePoints(values, points=40):
        distributeValues(
            values,
            keyGetter=Skill.getKey,
            countGetter=Skill.getCount,
            incrementor=Skill.increment,
            total=point,
        )
