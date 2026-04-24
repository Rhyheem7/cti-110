# Rhyheem Rushing
# 04/23/2026
# P4HW1
# Collects user scores, validates input, drops the lowest, computes the average, and assigns a letter grade.


# Ask user how many scores they want to enter
num = int(input("How many scores do you want to enter? "))

# Create empty list to store scores
scores = []

# Loop to collect scores
for i in range(num):
    # Ask for a score
    s = float(input(f"\nEnter score #{i+1}: "))
    
    # Validate score (must be between 0 and 100)
    while s < 0 or s > 100:
        print("\nINVALID Score entered!!!!")
        print("Score should be between 0 and 100")
        s = float(input(f"Enter score #{i+1} again: "))
    
    # Add valid score to list
    scores.append(s)

# Find the lowest score
low = min(scores)

# Remove the lowest score from the list
scores.remove(low)

# Calculate the average of remaining scores
avg = sum(scores) / len(scores)

# Determine the letter grade
if avg >= 90:
    grade = "A"
elif avg >= 80:
    grade = "B"
elif avg >= 70:
    grade = "C"
elif avg >= 60:
    grade = "D"
else:
    grade = "F"

# Display results
print("\n--------------Results--------------")
print(f"Lowest Score  : {low}")
print(f"Modified List : {scores}")
print(f"Scores Average: {avg:.2f}")
print(f"Grade         : {grade}")
print("-----------------------------------")