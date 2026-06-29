class BankAccount:
    def __init__(self,balance=0.0):
        self.balance = balance
    @property
    def balance(self):
        return self._balance
    @balance.setter
    def balance(self, value):
        if value < 0:
            raise ValueError("Balance cannot be negative")
        self._balance = value

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposited: ${amount:.2f}. New balance: ${self.balance:.2f}")

    def withdraw(self, amount):
        if 0 < amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: ${amount:.2f}. New balance: ${self.balance:.2f}")
        else:
            print("Invalid withdrawal amount or insufficient funds.")

def main():
    account = BankAccount()
    withdraw = float(input("Enter the amount to withdraw: "))
    account.withdraw(withdraw)

if __name__ == "__main__":
    main()