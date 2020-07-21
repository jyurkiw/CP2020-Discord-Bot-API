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
    def docToSkills(doc, startingSkillLevel=1):
        if doc.get("select", None) and isinstance(doc.get("skill"), list):
            return [
                Skill(s, startingSkillLevel)
                for s in sample(doc.get("skill"), int(doc.get("select")))
            ]
        else:
            return [Skill(doc.get("skill"), startingSkillLevel)]

    @staticmethod
    def distributePoints(values, points=40):
        distributeValues(
            values,
            keyGetter=Skill.getKey,
            countGetter=Skill.getCount,
            incrementor=Skill.increment,
            points=points,
        )
