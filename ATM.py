#!/usr/bin/env python
# coding: utf-8

# ### ATM STIMULATION BY USING PYTHON

# In[ ]:


##### class Account:
    def __init__(self, card_number, pin, balance=0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance

    def deposit(self, amount):
        self.balance += amount
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            print(f"Withdrawal successful. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

def authenticate(card_number, pin, accounts):
    for account in accounts:
        if account.card_number == card_number and account.pin == pin:
            return account
    return None

accounts = [
    Account("123456", "1234", 1000),
    Account("654321", "4321", 500)
]

def main():
    card_number = input("Enter your card number: ")
    pin = input("Enter your PIN: ")
    account = authenticate(card_number, pin, accounts)
    if not account:
        print("Authentication failed.")
        return

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            amount = float(input("Enter the amount to deposit: "))
            account.deposit(amount)
        elif choice == "3":
            amount = float(input("Enter the amount to withdraw: "))
            account.withdraw(amount)
        elif choice == "4":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

