"""Tools and utilities for setting up the database in mongodb or amazon's
documentdb.
"""

import json
import pymongo
import os


def insert_collection_doc_data(filepath, filename):
    client = pymongo.MongoClient()
    db = client.cyberpunk2020

    with open(os.path.join(filepath, filename), "r") as f:
        data = json.loads(f.read())
        collection_name = filename.replace(".json", "")

        # Murder any existing collection and rebuild it.
        # This function should preserve nothing, and replace everything.
        db[collection_name].drop()
        db[filename.replace(".json", "")].insert_many(data)
