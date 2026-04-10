# Rhyheem Rushing
# Date: 4/7/2026
# Assignment: P2HW1
# Description: Enhances P1HW2 by formatting monetary values and aligning output neatly.



print("This program calculates and displays travel expenses\n")

# Use float instead of int
budget = float(input("Enter Budget: "))
destination = input("Enter your travel destination: ")
gas = float(input("How much do you think you will spend on gas? "))
accommodation = float(input("Approximately, how much will you need for accommodation/hotel? "))
food = float(input("Last, how much do you need for food? "))

# Calculate remaining balance
remaining_balance = budget - gas - accommodation - food

# Display formatted output
print("\n------------Travel Expenses------------")
print(f"{'Location:':<20}{destination}")
print(f"{'Initial Budget:':<20}${budget:,.2f}")
print()

print(f"{'Fuel:':<20}${gas:,.2f}")
print(f"{'Accommodation:':<20}${accommodation:,.2f}")
print(f"{'Food:':<20}${food:,.2f}")
print()

print("--------------------------------------")
print(f"{'Remaining Balance:':<20}${remaining_balance:,.2f}")