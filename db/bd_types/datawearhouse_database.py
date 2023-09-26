from .database import Database

class DataWearHouseConnection(Database):
    
    def connect(self, host: str, user: str, password: str, dbname: str, schema: str | None) -> None:
        return super().connect(host, user, password, dbname, schema)