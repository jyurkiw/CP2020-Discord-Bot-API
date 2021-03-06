"""Because of how much we were using JSON data, it became only natural to
think about using MongoDB or another compatable document database.
This is a standard interface for a MongoDB-style document database across this
application.
"""
import pymongo


class MongoHandler(object):
    def __init__(self, db_name, collection_name):
        self.client = pymongo.MongoClient()
        self.db = self.client[db_name]
        self.collection = self.db[collection_name]

    def getNRandom(self, filter, n):
        return list(
            self.collection.aggregate(
                [
                    {"$match": filter},
                    {"$sample": {"size": n}},
                    {"$project": {"_id": 0}},
                ]
            )
        )

    def getRandom(self, filter):
        r = self.getNRandom(filter, 1)
        if r:
            return r[0]
        else:
            return None
