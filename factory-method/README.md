# Payment Method Factory Pattern

This repository contains a Python code example that demonstrates the Factory Method design pattern to handle different payment methods like Credit Card, PayPal, and Google Pay.

## Table of Contents

- [Overview](#overview)
- [Classes](#classes)
  - [Payment](#payment)
  - [CreditCardPayment](#creditcardpayment)
  - [GooglePayPayment](#googlepaypayment)
  - [PaypalPayment](#paypalpayment)
  - [PaymentMethod](#paymentmethod)
  - [PaymentFactory](#paymentfactory)
- [Main Function](#main-function)
- [Running the Code](#running-the-code)

## Overview

The Factory Method design pattern is used to create an object without specifying the exact class of object that will be created. This example uses the Factory Method pattern to create a payment method based on the user's choice.

## Classes

### Payment

This is an abstract base class that defines the interface for all payment methods. It has an abstract method `pay` that takes an amount as an argument.

```python
from abc import ABC, abstractmethod
from decimal import Decimal

class Payment(ABC):
    
    @abstractmethod
    def pay(self, amount: Decimal):
        pass
```

### CreditCardPayment
This class inherits from the Payment abstract class and implements the pay method for credit card payments.

```python
from decimal import Decimal
from payment import Payment

class CreditCardPayment(Payment):
    
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merch using a Credit Card.")
```

### GooglePayPayment
This class inherits from the Payment abstract class and implements the pay method for Google Pay payments.

```python
from decimal import Decimal
from payment import Payment

class GooglePayPayment(Payment):
    
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merch using Google pay.")
```

### PaypalPayment
This class inherits from the Payment abstract class and implements the pay method for PayPal payments.

```python
from decimal import Decimal
from payment import Payment

class PaypalPayment(Payment):
    
    def pay(self, amount: Decimal):
        print(f"Successfully paid ${amount} to merch using Paypal.")

```

### PaymentMethod
This is an enumeration that defines the types of payment methods available.
```python
from enum import Enum

class PaymentMethod(Enum):
    CREDIT_CARD = 1
    PAYPAL = 2
    GOOGLE_PLAY = 3

```

### PaymentFactory
This is the factory class that creates and returns an instance of a payment method based on the user's choice.

```python
from payment import Payment
from payment_method import PaymentMethod
from credit_card_payment import CreditCardPayment
from paypal_payment import PaypalPayment
from google_play_payment import GooglePayPayment

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
```

### Main Function 
The main function demonstrates how to use the PaymentFactory to create a payment method and then make a payment.


```python
from payment_factory import PaymentFactory
from payment_method import PaymentMethod

def main ():
    payment = PaymentFactory.create(PaymentMethod.CREDIT_CARD)
    payment.pay(1000.00)
    
if __name__ == "__main__":
    main()

```

### Dynamic Payment Factory
The DynamicPaymentFactory class dynamically loads all the payment types and provides a method to create a payment object based on the type.

```python
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

```

### Running the Code
Running the Code
```python
python main.py
```

```bash
Successfully paid $1000.00 to merch using a Credit Card.
```