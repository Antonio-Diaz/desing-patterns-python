# from payment_factory import PaymentFactory
# from payment_method import PaymentMethod
from dynamic_payment_factory import DynamicPaymentFactory
from database_method import DatabaseMethod

def main ():
    # payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    factory = DynamicPaymentFactory()
    payment = factory.create("CreditCardPayment")
    payment.pay(1000.00)
    
if __name__ == "__main__":
    main()