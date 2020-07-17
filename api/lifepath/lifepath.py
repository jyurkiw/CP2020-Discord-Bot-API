from ..util.mongo.mongo_handler import MongoHandler
import pymongo
from random import choice


class LifepathRoller(MongoHandler):
    def __init__(self, db_name):
        super().__init__(db_name, "lifepath")

    def rollTable(self, step, tableName):
        return self.getRandom({"step": step, "table_name": tableName})

    def rollTableChain(self, step, startTableName):
        result = self.rollTable(step, startTableName)
        results = {result["table_name"]: result}

        while result.get("redirect", False):
            print("redirect", flush=True)
            redirect = choice(result["redirect"])
            if redirect in results:
                print("redirect error", flush=True)
                raise Exception(
                    "Circular lifepath redirection detected ({step}: {table_name}). Aborting...".format(
                        result
                    )
                )
            result = self.rollTable(step, redirect)
            print(result, flush=True)
            results[result["table_name"]] = result
        return results

    def isModuleResult(self, result):
        return result.get("module_key", False)
