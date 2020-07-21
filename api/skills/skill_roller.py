from .career_skills import CareerSkillsRoller
from .pickup_skills import PickupSkillsRoller

from random import choice


class SkillRoller(object):
    """Build a random skill list for wastables.
    Generates roles, career skills, and distributes pickup skill points.
    """

    def __init__(self, dbName):
        """Setup the roller with master skills, career skills, and roles.

        Params:
            masterSkills List The master skill list.
            careerSkills List Career skill lists grouped by roles.
            roles List A list of roles with career skill data.
        """
        self.csRoller = CareerSkillsRoller(dbName)
        self.psRoller = PickupSkillsRoller(dbName)

    def rollRandomRole(self, numPickupSkillPoints, points=40):
        """Returns a random set of skills, pickup skills, and a random role.

        Params:
            numPickupSkillPoints int The number of pickup skill points to distribute.
            points int The number of career skill points to distribute (default=40)

        Returns:
            (role, [Skill1, Skill2, ..., SkillN])
        """
        role = self.getRandomRole()
        return role, self.roll(role, numPickupSkillPoints)

    def roll(self, role, numPickupSkillPoints, points=40):
        """Returns a random set of skills and pickup skills for a role.

        Params:
            numPickupSkillPoints in The number of pickup skill points to distribute.
            point int The number of career skill points to distribute (default=40)
        """
        return self.psRoller.addPickupSkills(
            self.csRoller.getCareerSkills(role), numPickupSkillPoints
        )

    def getRandomRole(self):
        """Returns a random role.
        """
        return choice(self.csRoller.getRoles())
