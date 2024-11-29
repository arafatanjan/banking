class Banking:
    def __init__(self, user_name, initial_balance):
        self.name = user_name
        self.balance = initial_balance
    
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount!")
    
    def get_balance(self):
        return self.balance
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
            print(f"Withdrew: {amount}")
        else:
            print("Insufficient balance!")


def main():
    
    user_name = input("Enter your name: ")
    initial_balance = float(input("Enter initial balance: "))

   
    account = Banking(user_name, initial_balance)

    
    print(f"Account created for {user_name} with balance {account.get_balance()}")

    
    while True:
        print("\nOptions:")
        print("1. Deposit Money")
        print("2. Withdraw Money")
        print("3. Check Balance")
        print("4. Exit")
        
        choice = input("Enter choice (1/2/3/4): ")
        
        if choice == "1":
            deposit_amount = float(input("Enter amount to deposit: "))
            account.deposit(deposit_amount)
        elif choice == "2":
            withdraw_amount = float(input("Enter amount to withdraw: "))
            print(account.withdraw(withdraw_amount))
        elif choice == "3":
            print(f"Current balance: {account.get_balance()}")
        elif choice == "4":
            print("Thank you for using our banking system!")
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()