#Problem: Simulate a simple ATM machine where a user can perform multiple transactions until they choose to exit.


print("Simple ATM Machine")
print("0: Deposit money")
print("1: Withdraw money")

balance = 0

user_choice = input("Enter your choice ('exit' to quit): ")

while user_choice.lower() != 'exit':
    # application runs here until exit is given

    if user_choice == '0':
        # deposit money
        deposit_amount = int(input("Enter amount to deposit: "))
        balance += deposit_amount
        print("Your balance is: ", balance)
    elif user_choice == '1':
        # withdraw money
        withdraw_amount = int(input("Enter amount to withdraw: "))
        if withdraw_amount > balance:
            print("Insufficient bank balance.")
        else:
            balance -= withdraw_amount
            print("Your balance is: ", balance)

    user_choice = input("Enter your choice ('exit' to quit): ")
