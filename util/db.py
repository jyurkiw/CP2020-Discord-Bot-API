"""Tools and utilities for setting up the database in mongodb or amazon's
documentdb.
"""

import json
import pymongo
import os


def insert_collection_doc_data(
    filepath, filename, indexes=[], collection_name=None
):
    if not collection_name:
        collection_name = filename.replace(".json", "")

    client = pymongo.MongoClient()
    db = client.cyberpunk2020

    with open(os.path.join(filepath, filename), "r") as f:
        data = json.loads(f.read())

        # Murder any existing collection and rebuild it.
        # This function should preserve nothing, and replace everything.
        collection = db[collection_name]
        collection.drop()
        collection.insert_many(data)

        if indexes:
            for index in indexes:
                collection.create_index(index)


dataPath = "cyberpunk_discord_bot/data/"
insert_collection_doc_data(
    dataPath, "career_skills.json", ["stat", "role_name"]
)
insert_collection_doc_data(
    dataPath, "master_skill_list.json", ["stat"], "skills"
)
insert_collection_doc_data(dataPath, "lifepath.json", ["step", "table_name"])
insert_collection_doc_data(
    dataPath,
    "weapons.json",
    [
        "category",
        "type",
        "concealability",
        "availability",
        "ammo_type",
        "reliability",
    ],
)
insert_collection_doc_data(
    dataPath, "armor.json", ["head", "torso", "arms", "legs"]
)
