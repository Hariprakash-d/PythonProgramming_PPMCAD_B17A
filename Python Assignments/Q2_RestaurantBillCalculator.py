"""
---------------------------------------------------------------
Author: Hari Prakash D (ID: 14313, Batch-17A)
Date: 13-APR-2026
---------------------------------------------------------------

Restaurant Bill Calculator:

Write a Python program that calculates the total restaurant bill including service charge, tax, and tip.
The program should:
    1. Take the meal cost as input from the user.
    2. Tip is fixed at 5% of the meal cost.
    3. Service Charge: 10% of meal cost
    4. Amount after Service: Meal cost + Service charge
    5. Tax: 5% of amount after service
    6. Tip: 5% of amount after service
    7. Total Bill: Amount after service + Tax + Tip

"""

# Function to calculate the total bill
def calculate_total_bill(meal_cost):
    service_charge = 0.10 * meal_cost
    amount_after_service = meal_cost + service_charge
    tax = 0.05 * amount_after_service
    tip = 0.05 * amount_after_service
    total_bill = amount_after_service + tax + tip

    print(f"Meal Cost: {meal_cost}")
    print(f"Service Charge (10%): {service_charge:.2f}")
    print(f"Amount after Service: {amount_after_service:.2f}")
    print(f"Tax (5%): {tax:.2f}")
    print(f"Tip (5%): {tip:.2f}")
    print(f"Total Bill: {total_bill:.2f}")

    return total_bill

# Get user input for meal cost
meal_cost = float(input("Enter the meal cost: "))
# Calculate the total bill
total_bill = calculate_total_bill(meal_cost)
# Print the total bill
print(f"Return: {total_bill:.2f}")

