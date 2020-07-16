from .mongo_handler import MongoHandler
import pymongo


class WeaponsHandler(MongoHandler):
    def __init__(self):
        client = pymongo.MongoClient()
        super().__init__(client, client.cyberpunk2020)
        self.weapons = self.db.weapons

    def getRandomWeapon(self, category):
        return self.getRandom(self.weapons, {"category": category})
