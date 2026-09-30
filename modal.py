class Transaction:
    def ___init___(self , month, amount, transaction_type):
        self.month = month
        self.amount = amount
        self.transactionj_type = transaction_type

        def show(self):
            print("Month:",self.month)
            print("Type:",self.transaction_type)
            print("Amount:",self.amount)
