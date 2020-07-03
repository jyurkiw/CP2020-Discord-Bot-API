# Constants file for the data handler json format
class JsonConstants(object):
    default = "Default"

    # Header Names
    tableName = "name"
    actionType = "action_type"
    redirect = "redirect"
    tableData = "table_data"
    moduleKey = "module_key"

    # Action Types
    simple = "simple"
    redirectData = "redirect-data"
    redirectTable = "redirect-table"
    executeModule = "execute-module"

    # Data Keys
    value = "value"
