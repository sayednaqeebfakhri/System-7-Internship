from Bank_account import BankAccount

# Create a bank account instance
account = BankAccount("123456789", "John Doe", 1000)

# Display account information
account.display_account_info()

# Deposit money
account.deposit(500)

# Withdraw money
account.withdraw(200)


# Check balance
current_balance = account.get_balance()
print(f"Current Balance: {current_balance}")

