# Check account balance
# Do you want to see account balance?
# Do you want to withdrawl


# ATM Machine

# Define account balance
bank = "Git Hub Bank"
accnt_balance = 300.00
view_balance = "y"
withdrawl = "y"

print(f"Welcome to {bank}!")
view_balance = input("Would you like to view your balance today?(y/n): ")
if view_balance == "y":
    print(f"Great you currently have ${accnt_balance} in your account.")
    withdrawl = input("Would you like to make a withdrawl?(y/n): ")
    if withdrawl == "y":
        print(f"How much would you like to withdrawl?")
        withdrawl_amnt = int(input("Enter amount $: "))
        accnt_balance = accnt_balance - withdrawl_amnt
        if withdrawl_amnt < accnt_balance:
            print("Sorry insufficient funds")
        else:
            print(f"Your remaining balance is ${accnt_balance:,.2f}")
            print(f"Thank you for comming in to {bank}, Have a wonderful day!")
    else:
        print(f"Thank you for comming in to {bank}, Have a wonderful day!")
else:
    withdrawl = input(f"Would you like to make a withdrawl?(y/n): ")

print("Thanks for looking at my ATM. The end :)")