from inspect import getmembers, isclass, isabstract
import payment_types

class DynamicPaymentFactory(object):
    payment_dict = {}
    
    def __init__(self) -> None:
        self.load_payment_types()
    
    def load_payment_types(self):
        members = getmembers(payment_types, lambda m: isclass(m) and not isabstract(m))
        for name, _type in members:
            if isclass(_type) and issubclass(_type, payment_types.Payment):
                self.payment_dict[name] = _type
    
    def create(self, payment_type: str):
        if payment_type in self.payment_dict:
            return self.payment_dict[payment_type]()
        else:
            raise ValueError(f"{payment_type} is not currently supported")