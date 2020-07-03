class TableResult(object):
    """Simple table result storage object.
    """

    def __init__(self, name, value):
        self.name = name
        self.value = value

    def __str__(self):
        if type(self.value) == list:
            return "{0}:\n\t{1}".format(
                self.name, "\n\t".join([i for i in self.value])
            )
        else:
            return "{0}: {1}".format(self.name, self.value)

    def isTableResult(self):
        return True
