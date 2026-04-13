current_balance = 5000

def atm_withdrawal(withdrawal_amount, account_balance):
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False
    
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be a multiple of 500")
        return False
    
    if withdrawal_amount > account_balance:
        print(f"Error: Insufficient funds. Available: {account_balance}")
        return False
    else:
        account_balance -= withdrawal_amount
        print(f"Withdrawal successful. Amount: {withdrawal_amount}")
        print(f"Remaining balance: {account_balance}")
        return True

amount = int(input("Enter the amount to withdraw: "))
result = atm_withdrawal(amount, current_balance)
print("Transaction result:", result)
print("Transaction completed. Thank you for using our ATM service.")

