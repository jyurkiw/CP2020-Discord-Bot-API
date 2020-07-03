from collections import deque
from random import choice
from .table_result import TableResult
from .redirect_action_result import RedirectActionResult
from .json_constants import JsonConstants as jc

import json


class CPDataHandler(object):
    def __init__(self, filename):
        self.dataFileName = filename
        with open(filename, "r") as filedata:
            self.data = json.loads(filedata.read())
        self.registeredModules = dict()

    def runProcess(self):
        actionList = deque(self.data[jc.default])
        resultList = list()

        while actionList:
            action = actionList.popleft()
            result = self.rollOnTable(action)

            if not result.isTableResult():
                actionList.appendleft(result.redirectKey)

            resultList.append(result)

        return resultList

    def rollOnTable(self, tableKey):
        if tableKey not in self.data:
            raise Exception("'{0}' not found in loaded data.".format(tableKey))

        if jc.actionType not in self.data[tableKey]:
            raise Exception(
                "'{0}' not found in loaded table ({1}).".format(
                    jc.actionType, tableKey
                )
            )

        tableAction = self.data[tableKey][jc.actionType]

        if tableAction == jc.simple:
            return self._getResult(tableKey)
        elif tableAction == jc.redirectData:
            return self._getRedirectData(tableKey)
        elif tableAction == jc.redirectTable:
            return self._getRedirectTable(tableKey)
        elif tableAction == jc.executeModule:
            if jc.moduleKey not in self.data[tableKey]:
                raise Exception(
                    "'{0}' not found in loaded table ({1})".format(
                        jc.moduleKey, tableKey
                    )
                )
            moduleKey = self.data[tableKey][jc.moduleKey]
            if moduleKey not in self.registeredModules:
                raise Exception(
                    "'" + moduleKey + "' not found in registered modules."
                )
            return self.registeredModules[moduleKey].runProcess()
        else:
            raise Exception(
                "Unrecognized action_type for table {0}: {1}".format(
                    tableKey, tableAction
                )
            )

    def registerRollModule(self, moduleKey, module):
        """Register a roll module with this data handler.
        module is a class pointer (ex: if you wanted to register the module
        Foo, you would pass in Foo such that Foo(self) could be executed
        by the data handler to create a foo object)

        Modules must implement a 'runProcess' function that takes no arguments.
        """
        self.registeredModules[moduleKey] = module(self)

    def _getResult(self, tableKey):
        if tableKey not in self.data:
            raise Exception("'{0}' not found in loaded data.".format(tableKey))
        if jc.tableName not in self.data[tableKey]:
            raise Exception(
                "'{0}' not found in loaded table ({1}).".format(
                    jc.tableName, tableKey
                )
            )
        return TableResult(
            self.data[tableKey][jc.tableName],
            choice(self.data[tableKey][jc.tableData]),
        )

    def _getRedirectData(self, tableKey):
        if tableKey not in self.data:
            raise Exception("'{0}' not found in loaded data.".format(tableKey))
        if jc.tableName not in self.data[tableKey]:
            raise Exception(
                "'{0}' not found in loaded table ({1}).".format(
                    jc.tableName, tableKey
                )
            )

        c = choice(self.data[tableKey][jc.tableData])

        if jc.value not in c:
            raise Exception(
                "'{0}' not found in loaded table data ({1}).".format(
                    jc.value, tableKey
                )
            )
        if jc.redirect not in c:
            raise Exception(
                "'{0}' not found in loaded table data ({1}).".format(
                    jc.redirect, tableKey
                )
            )

        return RedirectActionResult(
            self.data[tableKey][jc.tableName],
            c[jc.value],
            choice(c[jc.redirect]),
        )

    def _getRedirectTable(self, tableKey):
        if tableKey not in self.data:
            raise Exception("'{0}' not found in loaded data.".format(tableKey))
        if jc.tableName not in self.data[tableKey]:
            raise Exception(
                "'{0}' not found in loaded table ({1}).".format(
                    jc.tableName, tableKey
                )
            )
        if jc.redirect not in self.data[tableKey]:
            raise Exception(
                "'{0}' not found in loaded table ({1}).".format(
                    jc.redirect, tableKey
                )
            )

        return RedirectActionResult(
            self.data[tableKey][jc.tableName],
            choice(self.data[tableKey][jc.tableData]),
            choice(self.data[tableKey][jc.redirect]),
        )
