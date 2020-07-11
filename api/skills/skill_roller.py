from ..util import ValueDistributor
from random import choice, sample, randint
from collections import namedtuple

from math import ceil

SkillEntry = namedtuple("SkillEntry", ["stat", "skill"])
SelectEntry = namedtuple("CareerEntry", ["stat", "skill", "select"])
RandomSkillsResult = namedtuple("RandomSkillsResult", ["role", "skills"])


class SkillRoller(object):
    """Build a random skill list for wastables.
    Generates roles, career skills, and distributes pickup skill points.
    """

    def __init__(self, masterSkills, careerSkills, roles):
        """Setup the roller with master skills, career skills, and roles.

        Params:
            masterSkills List The master skill list.
            careerSkills List Career skill lists grouped by roles.
            roles List A list of roles with career skill data.
        """
        self.masterSkills = [SkillEntry(**skill) for skill in masterSkills]
        self.careerSkills = {
            role: [
                SelectEntry(**s) if "select" in s else SkillEntry(**s)
                for s in careerSkills[role]
            ]
            for role in careerSkills
        }
        self.roles = roles

    def rollRandom(self, numPickupSkillPoints):
        role = self.getRandomRole()
        return RandomSkillsResult(
            role=role, skills=self.roll(role, numPickupSkillPoints)
        )

    def roll(self, role, numPickupSkillPoints):
        distributor = self._buildCareerSkillDistributor(role)
        distributor.roll(totalRolls=40)
        self._addPickupSkills(distributor, numPickupSkillPoints)
        distributor.roll(numPickupSkillPoints)

        return distributor.getValueCounts()

    def getRandomRole(self):
        """Returns a random role.
        """
        return choice(self.roles)

    def _getCareerSkillList(self, role):
        skills = list()
        for s in self.careerSkills[role]:
            if isinstance(s, SkillEntry):
                skills.append(s)
            else:
                skills += [
                    SkillEntry(stat=s.stat, skill=skill)
                    for skill in sample(s.skill, k=s.select)
                ]
        return skills

    def _getPickupSkillList(self, numPickupSkillPoints):
        numPickupSkills = randint(
            ceil(numPickupSkillPoints / 10), numPickupSkillPoints
        )
        return sample(self.masterSkills, numPickupSkills)

    def _buildCareerSkillDistributor(self, role):
        distributor = ValueDistributor(minCountPer=1)
        for skill in self._getCareerSkillList(role):
            distributor.add(skill.skill, 1, 1)
        return distributor

    def _addPickupSkills(self, skillDistributor, pickupSkillPoints):
        charSkillList = set(skillDistributor.getSkillNames())

        for skill in self._getPickupSkillList(pickupSkillPoints):
            if skill.skill not in charSkillList:
                skillDistributor.add(skill.skill, 1, 0)
