class PaymentMethod:
    def pay(self, amount):
        raise NotImplementedError


class CashPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} in Cash.")


class CreditCardPayment(PaymentMethod):
    def pay(self, amount):
        print(f"Paid ${amount} using Credit Card.")
