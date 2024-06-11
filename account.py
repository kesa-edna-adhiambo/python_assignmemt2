class Account:
    def __init__(self, number, pin, customer_name, transactions, overdraft_limit):
        self.number = number
        self.__pin = pin
        self.__balance = 0
        self.customer_name = customer_name
        self.transactions = []
        self.overdraft_limit = overdraft_limit
        self.__is_frozen = False
        self.minimum_balance = 0

# outputs the balance when correct pin is given
    def show_balance(self,pin):
        if pin == self.__pin:
            return self.__balance

        else:
            return "wrong pin"

# depositing money to an account
    def deposit(self, amount):
        self.__balance += amount
        print(f"{amount} has been deposited in your account.")

# withdrawing money from an accountion.
    def update_customer_details(self, new_name, 
    def withdraw(self, amount):
        if amount > self.__balance:
            print("Insufficient balance.")
        else:
            self.__balance -= amount
            print(f"{amount} has been withdrawn from your account.")

# checking balance
    def check_balance(self):
        print(f"Hi,{self.customer_name} your Current balance is {self.__balance}.")

# Method to display the account owner's details and current balance
    def customer_details(self):
        print("Name:", self.customer_name)
        print("Account Number:", self.number)
        print(f"Balance: {self.__balance}\n")

# Method to update the account owner's information.
    def update_customer_details(self, new_name, new_number, new_pin):
        self.customer_name = new_name
        self.number = new_number
        self.__pin = new_pin


# Account Statement: Method to generate a statement of recent transactions.
    def add_transaction(self, amount, description):
        self.transactions.append({'amount': amount, 'description': description})

    def generate_statement(self):
        print("\tAmount\tDescription")
        for transaction in self.transactions:
            print(f"\t{transaction['amount']}\t{transaction['description']}")

# Set Overdraft Limit: Method to set an overdraft limit for the account.
    def set_overdraft_limit(self, amount):
        if amount <= self.__balance + self.overdraft_limit:
            self.__balance -= amount
            return True 
        else:
            self.__balance -= 10 
            return False 
     
# Interest Calculation: Method to calculate and apply interest to the balance.

    def apply_interest(self, interest_rate):
        interest = self.__balance * (interest_rate / 100)
        self.__balance += interest
        print(f"Interest of {interest} has been applied to your account.")    

# Freeze/Unfreeze Account: Methods to freeze and unfreeze the account for security reasons.
    def freeze_account(self):
        self.__is_frozen = True
        print("Your account has been frozen for security reasons.")

    def unfreeze_account(self):
        self.__is_frozen = False
        print("Your account has been unfrozen and is now active.")

    def transact_withdrawal(self, amount):
        if self.__is_frozen:
            print("Your account is frozen. Withdrawal cannot be processed.")
    
# Transaction History: Method to retrieve the history of all transactions made on the account.
    def get_transaction_history(self):
        if not self.transactions:
            print("No transactions found.")
            return []
        else:
            print("Transaction History:")
            print("\tAmount\tDescription")
            for transaction in self.transactions:
                print(f"\t{transaction['amount']}\t{transaction['description']}")
            return self.transactions

# Set Minimum Balance: Method to enforce a minimum balance requirement.
    def set_minimum_balance(self, amount):
        self.minimum_balance = amount
        print(f"The minimum balance has been set to {self.minimum_balance}.")

    def withdraw_money(self, amount):
        if self.__is_frozen:
            print("Your account is frozen. Withdrawal cannot be processed.")
        elif amount > self.__balance - self.minimum_balance:
            print(f"Insufficient balance. You must maintain a minimum balance of {self.minimum_balance}.")
        else:
            self.__balance -= amount
            print(f"{amount} has been withdrawn from your account.")
            self.add_transaction(-amount, "Withdrawal")

# Transfer Funds: Method to transfer funds from one account to another.
    def transfer_funds(self, target_account, amount):
        if self.__is_frozen:
            print("Your account is frozen. Transfer cannot be processed.")
            return False
        elif target_account.__is_frozen:
            print("The target account is frozen. Transfer cannot be processed.")
            return False
        elif amount > self.__balance - self.minimum_balance:
            print(f"Insufficient balance. You must maintain a minimum balance of {self.minimum_balance}.")
            return False
        else:
            self.__balance -= amount
            target_account.__balance += amount
            self.add_transaction(-amount, "Transfer Out")
            target_account.add_transaction(amount, "Transfer In")
            print(f"{amount} has been transferred to account number {target_account.number}.")
            return True
    
# Close Account: Method to close the account and perform necessary cleanup.
    def close_account(self, pin):
        if pin != self.__pin:
            print("Incorrect PIN. Account closure failed.")
            return False
        elif self.__is_frozen:
            print("Your account is frozen. Account closure cannot be processed.")
            return False
        else:
            self.__balance = 0
            self.transactions.clear()
            self.__is_frozen = True 
            print(f"Account number {self.number} belonging to {self.customer_name} has been closed.")
            return True

