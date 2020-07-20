from random import choice, sample, randint

from math import ceil


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
        pass

    def rollRandom(self, numPickupSkillPoints):
        pass

    def roll(self, role, numPickupSkillPoints):
        pass

    def getRandomRole(self):
        """Returns a random role.
        """
        pass
