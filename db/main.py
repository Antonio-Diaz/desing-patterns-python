from dynamic_database_factory import DynamicDatabaseFactory
from database_method import DatabaseMethod
def main ():
    host = 'host'
    user = 'user'
    password = 'password'
    dbname = 'dbname'
    schema = 'public'
    # payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    factory = DynamicDatabaseFactory()
    dwh_instance = factory.create(DatabaseMethod.DWH)
    dwh_instance.connect(host, user, password, dbname, schema)
    
if __name__ == "__main__":
    main()