from .table_result import TableResult


class RedirectActionResult(TableResult):
    """Simple Table Result storage object with redirection outcome.
    """

    def __init__(self, name, value, redirectKey):
        super().__init__(name, value)
        self.redirectKey = redirectKey

    def isTableResult(self):
        return False
