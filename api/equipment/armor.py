from ..util.mongo.mongo_handler import MongoHandler
from random import randint

_locations = ["head", "torso", "arms", "legs"]


class ArmorRoller(MongoHandler):
    def __init__(self, db_name):
        super().__init__(db_name, "armor")

    @staticmethod
    def getProtectedLocations(armorList):
        locations = {l: False for l in _locations}
        for armor in armorList:
            for location in _locations:
                locations[location] = locations[location] or armor[location]
        return locations

    @staticmethod
    def getArmorFilter(armorList):
        protectedLocations = ArmorRoller.getProtectedLocations(armorList)
        return {
            "$and": [
                {location: False}
                for location in protectedLocations
                if protectedLocations[location]
            ]
        }

    def getArmor(self, maxRolls=2):
        """Returns a list of armor 1-3 items long that makes sense.
        Won't double-up armor on locations.
        """
        if maxRolls == 0:
            return []

        armor = [self.getRandom({})]

        if maxRolls == 1:
            return armor

        protectedLocations = ArmorRoller.getProtectedLocations(armor)
        armor += [self.getRandom(ArmorRoller.getArmorFilter(armor))]

        if maxRolls == 2:
            return armor

        protectedLocations = ArmorRoller.getProtectedLocations(armor)
        armor += [self.getRandom(ArmorRoller.getArmorFilter(armor))]

        # Filter the return value because if no armor can be selected
        # (for example, if choice #1 was metal gear) then getRandom
        # will return None and [None] will be added to the armorList.
        return [a for a in armor if a]

    def getRandomArmor(self):
        """Returns a list of armor between 1 and 3 items long (random range).
        """
        return getArmor(randint(1, 3))
