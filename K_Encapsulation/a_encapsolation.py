class BankAccount:
    def __int__(self):
        self._balance = 0

    def deposit(self, amount):
        self._balance += amount

    def get_balance(self):
        return self._balance


acc = BankAccount()
acc.deposit(100)
print(acc)
print(acc._balance())
