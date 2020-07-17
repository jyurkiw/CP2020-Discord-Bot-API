from ..util.mongo.mongo_handler import MongoHandler


class WeaponsRoller(MongoHandler):
    def __init__(self, db_name):
        super().__init__(db_name, "weapons")

    def getRandomWeapon(self, category):
        return self.getRandom({"category": category})

    def getWeaponCategories(self):
        return self.collection.distinct("category")
