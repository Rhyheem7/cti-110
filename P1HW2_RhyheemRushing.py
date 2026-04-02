# Rhyheem Rushing
# 02 April 2026
# Travel budget
# This program calculates and displays travel expenses

print("This program calculates and displays travel expenses")
print()

budget = int(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = int(input("How much do you think you will spend on gas? "))
accommodation = int(input("Approximately, how much will you need for accommodation/hotel? "))
food = int(input("Last, how much do you need for food? "))

remaining_balance = budget - gas - accommodation - food

print()
print("--------Travel Expenses--------")
print("Location:", destination)
print("Initial Budget:", budget)
print()
print("Fuel:", gas)
print("Accommodation:", accommodation)
print("Food:", food)
print()
print("Remaining Balance:", remaining_balance)