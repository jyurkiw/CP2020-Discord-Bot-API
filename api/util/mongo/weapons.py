from mongo_handler import MongoHandler


class WeaponsHandler(MongoHandler):
    def __init__(self, client, database):
        super().__init__(client, database)
        self.weapons = self.database.weapons

    def getRandomWeapon(self, category):
        return self.getRandom(self.weapons, {"category": category})
