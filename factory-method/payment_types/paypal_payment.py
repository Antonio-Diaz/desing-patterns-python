from decimal import Decimal
from .payment import Payment

class PaypalPayment(Payment):
    
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merch using Paypal.")
        