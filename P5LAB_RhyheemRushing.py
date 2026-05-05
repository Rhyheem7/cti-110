# Rhyheem Rushing
# 05/04/2026
# P5LAB
# Self-checkout change calculator

import random

def disperse_change(change):
    cents = int(change * 100)

    dollars = cents // 100
    cents = cents % 100

    quarters = cents // 25
    cents = cents % 25

    dimes = cents // 10
    cents = cents % 10

    nickels = cents // 5
    cents = cents % 5

    pennies = cents

    print()
    if dollars > 0:
        print(dollars, "Dollars")
    if quarters > 0:
        print(quarters, "Quarters")
    if dimes > 0:
        print(dimes, "Dimes")
    if nickels > 0:
        print(nickels, "Nickels")
    if pennies > 0:
        print(pennies, "Pennies")

def main():
    amount_owed = round(random.uniform(0.01, 100.00), 2)
    print(f"You owe ${amount_owed}")

    cash = float(input("How much cash will you put in the self-checkout? "))

    change = round(cash - amount_owed, 2)
    print(f"Change is: ${change}\n")

    disperse_change(change)

main()