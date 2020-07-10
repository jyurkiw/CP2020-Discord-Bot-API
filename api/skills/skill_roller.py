from ..util import ValueDistributor
from random import choice, sample, randint
from collections import namedtuple

from math import ceil

SkillEntry = namedtuple("SkillEntry", ["stat", "skill"])
SelectEntry = namedtuple("CareerEntry", ["stat", "skill", "select"])


class SkillRoller(object):
    def __init__(self, masterSkills, careerSkills, roles):
        self.masterSkills = [SkillEntry(**skill) for skill in masterSkills]
        self.careerSkills = {
            role: [
                SelectEntry(**s) if "select" in s else SkillEntry(**s)
                for s in careerSkills[role]
            ]
            for roles in careerSkills
        }
        self.roles = roles

    def _getRandomRole(self):
        return choice(self.roles)

    def _getCareerSkillList(self, role):
        return self.careerSkills[role]

    def _getPickupSkillList(self, numPickupSkillPoints):
        numPickupSkills = randint(
            ceil(numPickupSkillPoints / 10), numPickupSkillPoints
        )
        return sample(self.masterSkills, numPickupSkills)
