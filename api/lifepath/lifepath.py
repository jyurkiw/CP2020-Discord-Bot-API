from ..util.mongo.mongo_handler import MongoHandler
import pymongo
from random import choice
from collections import OrderedDict
from collections import namedtuple

Step = namedtuple("Step", ["step", "table"])


class LifepathRoller(MongoHandler):
    steps = [
        Step(step="Origins and Personal Style", table="Clothes"),
        Step(step="Family Background", table="Family Ranking"),
        Step(step="Motivations", table="Personality Traits"),
    ]

    def __init__(self, db_name):
        super().__init__(db_name, "lifepath")

    def rollLifepath(self):
        lifepath = OrderedDict()
        for step in LifepathRoller.steps:
            lifepath[step.step] = self._rollTableChain(step.step, step.table)

        return lifepath

    def _rollTable(self, step, tableName):
        return self.getRandom({"step": step, "table_name": tableName})

    def _rollTableChain(self, step, startTableName):
        result = self.rollTable(step, startTableName)
        results = [result]

        while result.get("redirect", False):
            redirect = choice(result["redirect"])
            if redirect in results:
                raise Exception(
                    "Circular lifepath redirection detected ({step}: {table_name}). Aborting...".format(
                        **result
                    )
                )
            result = self.rollTable(step, redirect)
            results.append(result)
        return results

    def isModuleResult(self, result):
        return result.get("module_key", False)
