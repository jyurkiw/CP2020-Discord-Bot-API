from random import randint, choice, choices
from ..lib.table_result import TableResult

SIBLING_AGE_KEY = "Sibling Age"
SIBLING_FEELINGS_KEY = "Sibling Feelings"


class SiblingsModule(object):
    def __init__(self, data_handler):
        self.dataHandler = data_handler

    def runProcess(self):
        numSiblings = self.numSiblings()
        if numSiblings:
            return TableResult(
                name="Siblings",
                value=[
                    "{0}, {1}, {2}".format(
                        self.rollSex(),
                        self.rollRelativeAge(),
                        self.rollSiblingFeelings(),
                    )
                    for i in range(0, numSiblings)
                ],
            )
        else:
            return TableResult("Siblings", "Only child")

    def numSiblings(self):
        roll = randint(1, 10)
        if roll <= 7:
            return roll
        else:
            return False

    def rollSex(self):
        return choice(["male", "female"])

    def rollRelativeAge(self):
        return self.dataHandler.rollOnTable(SIBLING_AGE_KEY).value

    def rollSiblingFeelings(self):
        return self.dataHandler.rollOnTable(SIBLING_FEELINGS_KEY).value
