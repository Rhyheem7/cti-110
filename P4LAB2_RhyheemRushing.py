run_again = "yes"

while run_again == "yes":

    num = int(input("Enter an integer: "))

    if num < 0:
        print("Cannot accept negative values.")

    else:
        for i in range(1, 13):
            print(f"{num} x {i} = {num * i}")

    run_again = input("Do you want to run again? (yes/no): ")

print("Exiting program...")