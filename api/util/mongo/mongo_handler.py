"""Because of how much we were using JSON data, it became only natural to
think about using MongoDB or another compatable document database.
This is a standard interface for a MongoDB-style document database.
"""
import pymongo


class MongoHandler(object):
    def __init__(self, client, database):
        self.client = client
        self.db = database

    def getNRandom(self, collection, filter, n):
        return collection.aggregate(
            [{"$match": filter}, {"$sample": {"size": n}}]
        )

    def getRandom(self, collection, filter):
        return self.getNRandom(collection, filter, 1)[0]
