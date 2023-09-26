from .database import Database

class ScraperConnection(Database):
    
    def connect(self, host: str, user: str, password: str, dbname: str, schema: str | None) -> None:
        return super().connect(host, user, password, dbname, schema)