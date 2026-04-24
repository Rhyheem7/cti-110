# Rhyheem Rushing
# 04/23/2026
# P4HW2
# Calculates pay for multiple employees and totals


# totals
total_ot = 0
total_reg = 0
total_gross = 0
count = 0

# first input
name = input("Enter employee's name or \"Done\" to terminate: ")

while name != "Done":
    
    hours = float(input("How many hours did " + name + " work? "))
    rate = float(input("What is " + name + "'s pay rate? "))
    
    # overtime check
    if hours > 40:
        ot_hours = hours - 40
        reg_pay = 40 * rate
        ot_pay = ot_hours * rate * 1.5
    else:
        ot_hours = 0
        reg_pay = hours * rate
        ot_pay = 0
    
    gross = reg_pay + ot_pay
    
    # totals
    total_ot = total_ot + ot_pay
    total_reg = total_reg + reg_pay
    total_gross = total_gross + gross
    count = count + 1
    
    # display like example
    print("\nEmployee name: ", name)
    print()
    print("Hours Worked  Pay Rate  OverTime  OverTime Pay  RegHour Pay  Gross Pay")
    print("-----------------------------------------------------------------------")
    
    print(hours, "      ", format(rate, ".2f"), "     ", ot_hours, "     ", 
          format(ot_pay, ".2f"), "       $"+format(reg_pay, ".2f"), 
          "       $"+format(gross, ".2f"))
    
    # next employee
    name = input("\nEnter employee's name or \"Done\" to terminate: ")

# final output
print()
print("Total number of employees entered:", count)
print("Total amount paid for overtime: $" + format(total_ot, ".2f"))
print("Total amount paid for regular hours: $" + format(total_reg, ".2f"))
print("Total amount paid in gross: $" + format(total_gross, ".2f"))