from payment import Payment
from payment_method import PaymentMethod
from credit_card_payment import CreditCardPayment
from paypal_payment import PaypalPayment
from google_play_payment import GooglePayPayment

# Creator
class PaymentFactory:
    
    @staticmethod
    def create(payment_method: PaymentMethod) -> Payment:
        match payment_method:
            case PaymentMethod.CREDIT_CARD:
                return CreditCardPayment()
            case PaymentMethod.PAYPAL:
                return PaypalPayment()
            case PaymentMethod.GOOGLE_PLAY:
                return GooglePayPayment()
            case _:
                raise ValueError(f"{payment_method} is not currently supported.")