from payment_factory import PaymentFactory
from payment_method import PaymentMethod

def main ():
    payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    payment.pay(1000.00)
    
if __name__ == "__main__":
    main()