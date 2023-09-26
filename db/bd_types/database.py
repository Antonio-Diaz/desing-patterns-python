from typing import Optional
from abc import ABC, abstractmethod

class Database(ABC):
    
    @abstractmethod
    def connect(self, host: str, user: str, password: str, 
                dbname: str, schema: Optional[str]) -> None:
        """Abstract method connect

        Args:
            host (str): url from instance
            user (str): user from BD
            password (str): passsword from BD
            dbname (str): db name target to connect
            schema (Optional[str]): schema or something default public
        """
        print(f"""\t\t  host: {host}\n
                  user: {user}\n
                  password: {password}\n
                  dbname: {dbname}\n
                  schema: {schema}
                  """)