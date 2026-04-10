# Rhyheem Rushing
# 08 April 2026
# P2HW2
# This program calculates grade statistics for six modules.


"""
Pseudocode (Detailed Algorithm):

1. Ask the user to enter grades for Module 1 through Module 6.
2. Store each grade in separate variables.
3. Put all grades into a list called module_grades.
4. Find:
   - Lowest grade using min()
   - Highest grade using max()
   - Sum using sum()
   - Average = sum / 6
5. Display results formatted exactly like the example.
"""

# Input
module1 = float(input("Enter grade for Module 1: "))
module2 = float(input("Enter grade for Module 2: "))
module3 = float(input("Enter grade for Module 3: "))
module4 = float(input("Enter grade for Module 4: "))
module5 = float(input("Enter grade for Module 5: "))
module6 = float(input("Enter grade for Module 6: "))

# Store in list
module_grades = [module1, module2, module3, module4, module5, module6]

# Calculations
lowest = min(module_grades)
highest = max(module_grades)
total = sum(module_grades)
average = total / len(module_grades)

# Output (MATCHES IMAGE EXACTLY)
print("\n------------Results------------")
print(f"Lowest Grade:         {lowest:.1f}")
print(f"Highest Grade:        {highest:.1f}")
print(f"Sum of Grades:        {total:.1f}")
print(f"Average:              {average:.2f}")
print("----------------------------------")