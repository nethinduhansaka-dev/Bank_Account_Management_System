class Account:
    def __init__(self, acc_number, initial_balance):
        self.acc_number = acc_number
        self.balance = initial_balance

    def deposit(self, amount):
        if amount < 0:
            print("Deposit amount must be non-negative.")
        else:
            self.balance += amount
            print(f"Deposit of {amount} successfully made. Current balance: {self.balance}")

    def withdraw(self, amount):
        if amount < 0:
            print("Withdrawal amount must be non-negative.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            print(f"Withdrawal of {amount} successfully made. Current balance: {self.balance}")

    def transfer(self, amount, recipient):
        if amount < 0:
            print("Transfer amount must be non-negative.")
        elif amount > self.balance:
            print("Insufficient balance.")
        else:
            self.balance -= amount
            recipient.balance += amount
            print(f"Transfer of {amount} to account {recipient.acc_number} successful.")
            print(f"Sender's balance: {self.balance}, Recipient's balance: {recipient.balance}")


class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, initial_balance):
        if acc_number in self.accounts:
            print("Account already exists.")
        else:
            self.accounts[acc_number] = Account(acc_number, initial_balance)
            print("Account created successfully.")

    def get_account(self, acc_number):
        if acc_number in self.accounts:
            return self.accounts[acc_number]
        else:
            print("Account not found.")
            return None



bank = Bank()
print("\n                 ....Bank Account Management System....            ")
while True:
    print("\n1. Create Account\n2. Deposit\n3. Withdraw\n4. Check Balance\n5. Transfer\n6. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        acc_number = input("Enter account number: ")
        if acc_number.isdigit():
            initial_balance = float(input("Enter initial balance: "))
            bank.create_account(acc_number, initial_balance)
        else:
            print("\nAccount number should be numbers only.\n")

    elif choice == '2':
        acc_number = input("Enter account number: ")
        if acc_number.isdigit():
            account = bank.get_account(acc_number)
            if account:
                amount = float(input("Enter deposit amount: "))
                account.deposit(amount)
        else:
            print("\nAccount number should be numbers only.\n")

    elif choice == '3':
        acc_number = input("Enter account number: ")
        if acc_number.isdigit():
            account = bank.get_account(acc_number)
            if account:
                amount = float(input("Enter withdrawal amount: "))
                account.withdraw(amount)
        else:
            print("\nAccount number should be numbers only.\n")

    elif choice == '4':
        acc_number = input("Enter account number: ")
        if acc_number.isdigit():
            account = bank.get_account(acc_number)
            if account:
                print(f"Account balance: {account.balance}")
        else:
            print("\nAccount number should be numbers only.\n")

    elif choice == '5':
        sender_acc_number = input("Enter sender's account number: ")
        if sender_acc_number.isdigit():
            sender_account = bank.get_account(sender_acc_number)
            if sender_account:
                recipient_acc_number = input("Enter recipient's account number: ")
                if recipient_acc_number.isdigit():
                    recipient_account = bank.get_account(recipient_acc_number)
                    if recipient_account:
                        amount = float(input("Enter transfer amount: "))
                        sender_account.transfer(amount, recipient_account)
                else:
                    print("\nAccount number should be numbers only.\n")
        else:
            print("\nAccount number should be numbers only.\n")

    elif choice == '6':
        print("Exiting program.")
        break

    else:
        print("Invalid choice. Please try again.")

