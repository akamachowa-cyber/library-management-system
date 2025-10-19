from payment import PaymentMethod

class LibraryService:
    def __init__(self, payment_method: PaymentMethod):
        self.payment_method = payment_method

    def pay_fine(self, amount):
        self.payment_method.pay(amount)
