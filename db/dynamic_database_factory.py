from inspect import getmembers, isclass, isabstract
import bd_types

class DynamicDatabaseFactory(object):
    database_connection = {}
    
    def __init__(self) -> None:
        self.load_db_types()
    
    def load_db_types(self):
        members = getmembers(bd_types, lambda m: isclass(m) and not isabstract(m))
        for name, _type in members:
            if isclass(_type) and issubclass(_type, bd_types.Database):
                self.database_connection[name] = _type
    
    def create(self, database_type: str):
        if database_type in self.database_connection:
            return self.database_connection[database_type]()
        else:
            raise ValueError(f"{database_type} is not currently Supported.")