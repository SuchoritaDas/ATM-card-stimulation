from datetime import datetime

class Account:
    def __init__(self, card_number, pin, balance=0):
        self.card_number = card_number
        self.pin = pin
        self.balance = balance
        self.transactions = []

    def deposit(self, amount):
        self.balance += amount
        self.transactions.append(f"{datetime.now()}: Deposited {amount}. New balance: {self.balance}")
        print(f"Deposit successful. New balance: {self.balance}")

    def withdraw(self, amount):
        if amount > self.balance:
            print("Insufficient funds.")
        else:
            self.balance -= amount
            self.transactions.append(f"{datetime.now()}: Withdrew {amount}. New balance: {self.balance}")
            print(f"Withdrawal successful. New balance: {self.balance}")

    def check_balance(self):
        print(f"Current balance: {self.balance}")

    def print_transactions(self):
        print("Transaction History:")
        for transaction in self.transactions:
            print(transaction)

    def change_pin(self):
        import getpass
        old_pin = getpass.getpass("Enter your current PIN: ")
        if old_pin == self.pin:
            new_pin = getpass.getpass("Enter your new PIN: ")
            new_pin_confirm = getpass.getpass("Confirm your new PIN: ")
            if new_pin == new_pin_confirm:
                self.pin = new_pin
                print("PIN change successful.")
            else:
                print("New PINs do not match. PIN change failed.")
        else:
            print("Incorrect current PIN. PIN change failed.")

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
    import getpass
    card_number = input("Enter your card number: ")
    pin = getpass.getpass("Enter your PIN: ")
    account = authenticate(card_number, pin, accounts)
    if not account:
        print("Authentication failed.")
        return

    while True:
        print("\n1. Check Balance\n2. Deposit\n3. Withdraw\n4. View Transactions\n5. Change PIN\n6. Exit")
        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            account.check_balance()
        elif choice == "2":
            try:
                amount = float(input("Enter the amount to deposit: "))
                account.deposit(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "3":
            try:
                amount = float(input("Enter the amount to withdraw: "))
                account.withdraw(amount)
            except ValueError:
                print("Invalid input. Please enter a numeric value.")
        elif choice == "4":
            account.print_transactions()
        elif choice == "5":
            account.change_pin()
        elif choice == "6":
            print("Thank you for using the ATM. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
