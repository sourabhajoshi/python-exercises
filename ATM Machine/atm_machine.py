import time

# Initial setup
balance_amt = 10000
password = 1234

# Insert card prompt
print("Please insert your debit card")
time.sleep(3)

# PIN input
pin = int(input("Please enter your PIN: "))

if pin == password:
    while True:
        print("""\nPlease choose an option:
                 1. Balance
                 2. Withdraw
                 3. Deposit
                 4. Exit""")

        try:
            option = int(input("Enter your choice: "))
        except ValueError:
            print("Please select a valid option.")
            continue

        if option == 1:
            print(f"The available balance is {balance_amt}")

        elif option == 2:
            try:
                withdraw_amt = int(input("Please enter the withdraw amount: "))
                if balance_amt >= withdraw_amt:
                    balance_amt -= withdraw_amt
                    print(f"Withdraw successful, and updated balance is {balance_amt}")
                else:
                    print("Insufficient funds to withdraw.")
            except ValueError:
                print("Please enter a valid amount.")

        elif option == 3:
            try:
                deposit_amt = int(input("Please enter the deposit amount: "))
                balance_amt += deposit_amt
                print(f"Deposit successful, updated balance is {balance_amt}")
            except ValueError:
                print("Please enter a valid amount.")

        elif option == 4:
            print("Thank you for using our ATM. Goodbye!")
            break

        else:
            print("Invalid choice! Please try again.")
else:
    print("Entered incorrect PIN, please try again.")
