# ATM Machine

# Define account balance
bank = "Git Hub Bank"
accnt_balance = 7125.00
thank_you = (f"---Thank you for comming in to {bank}, Have a wonderful day!---")

# Display welcome message
print(f"---Welcome to, {bank}!---")

# if-else statement if user wants to view balance then withdrawl
view_balance = input("Would you like to view your balance today?(y/n): ")
if view_balance == "y":
    print(f"Great you currently have ${accnt_balance} in your account.")
    withdrawl = input("Would you like to make a withdrawl?(y/n): ")
    if withdrawl == "y":
        print(f"    -How much would you like to withdrawl?")
        withdrawl_amnt = float(input("Enter amount $:"))
        new_balance = accnt_balance - withdrawl_amnt        # Calculation post withdrawl                              
        if withdrawl_amnt > new_balance:                # Cannot withdralw more than 
            print("Sorry insufficient funds")           # Account balance
            withdrawl_amnt = float(input("Enter another amount $:"))
        else:
            print(f"Your remaining balance is ${new_balance:,.2f}")
            print(thank_you)                                  
    else:
        print(thank_you)

# if-elif-else statement if user does not want to view balance and just withdrawl
elif view_balance == "n":
    withdrawl = input(f"Would you like to make a withdrawl?(y/n): ")
if withdrawl == "y":
    print(f"How much would you like to withdrawl?")
    withdrawl_amnt = float(input("Enter amount $:"))
    new_balance = accnt_balance - withdrawl_amnt        # Calculation post withdraw
    if withdrawl_amnt > new_balance:                 # Cannot withdrawl more than 
        print("Sorry insufficient funds")               # Account balance user protection
        withdrawl_amnt = float(input("Enter another amount $:")) # with while loop.
    else:
        print(f"Your remaining balance is ${new_balance:,.2f}")
        print(thank_you)

print("*** Thanks for looking at my ATM. The end :) ***")