balance = 1000  # Initial balance

while True:
    print("\n--- Welcome to the ATM ---")
    print("1. Check Balance")
    print("2. Deposit Money")
    print("3. Withdraw Money")
    print("4. Exit")

    choice = input("Select an option (1-4): ")

    if choice == "1":
        print(f"Your current balance is: ${balance}")

    elif choice == "2":
        amount = float(input("Enter the amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"${amount} has been deposited. New balance: ${balance}")
        else:
            print("Please enter a valid amount.")

    elif choice == "3":
        amount = float(input("Enter the amount to withdraw: "))
        if 0 < amount <= balance:
            balance -= amount
            print(f"${amount} has been withdrawn. New balance: ${balance}")
        else:
            print("Insufficient balance or invalid amount.")

    elif choice == "4":
        print("Thank you for using the ATM. Have a great day!")
        break

    else:
        print("Invalid choice. Please try again.")
