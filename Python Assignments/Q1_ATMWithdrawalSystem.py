"""
---------------------------------------------------------------
Author: Hari Prakash D (ID: 14313, Batch-17A)
Date: 13-APR-2026
---------------------------------------------------------------

ATM Withdrawal System:

A simple ATM withdrawal system in Python. The system should allow users to input the amount they wish to withdraw and 
check if the withdrawal is valid based on the following conditions:
    1. The withdrawal amount must be greater than 0.
    2. The withdrawal amount must be a multiple of 500.
    3. Account balance must be sufficient for withdrawal.

"""

# Initial account balance
account_balance = 5000

def atm_withdrawal(withdrawal_amount, current_balance):
    if withdrawal_amount <= 0:
        print("Error: Withdrawal amount must be greater than 0")
        return False
    
    if withdrawal_amount % 500 != 0:
        print("Error: Withdrawal amount must be a multiple of 500")
        return False
    
    if withdrawal_amount > current_balance:
        print(f"Error: Insufficient balance. Available: {current_balance}")
        return False
    else:
        current_balance -= withdrawal_amount
        print(f"Withdrawal successful. Amount: {withdrawal_amount}")
        print(f"Remaining balance: {current_balance}")
        return True
    
# Get user input for withdrawal amount
amount = int(input("Enter the amount to withdraw: "))
# Perform the withdrawal operation
result = atm_withdrawal(amount, account_balance)
print("Transaction result:", result)
print("Transaction completed. Thank you for using our ATM service.")
