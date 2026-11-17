"""
An online store supports multiple payment methods: CreditCard, UPI, and 
NetBanking. Create a base class Payment with a method process_payment() and 
override it in each payment type"""

class Payment:
    def process_payment(self):
        print("Processing payment...")

class CreditCard(Payment):
    def process_payment(self):
        print("Paid using Credit Card")

class UPI(Payment):
    def process_payment(self):
        print("Paid using UPI")

class NetBanking(Payment):
    def process_payment(self):
        print("Paid using Net Banking")

for p in [CreditCard(), UPI(), NetBanking()]:
    p.process_payment()
