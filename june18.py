# Start with a balance of 0
balance = 0.0

while True:
    # Show the menu
    print("\nWelcome to Your Bank!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    # Ask user for their choice
    choice = input("Choose an option (1-4): ")

    # Deposit money
    if choice == "1":
        amount = float(input("Enter amount to deposit: "))
        if amount > 0:
            balance += amount
            print(f"Deposited successfully! New balance: ${balance:.2f}")
        else:
            print("Invalid amount! Please enter a positive number.")

    # Withdraw money
    elif choice == "2":
        amount = float(input("Enter amount to withdraw: "))
        if amount > 0 and amount <= balance:
            balance -= amount
            print(f"Withdrawal successful! New balance: ${balance:.2f}")
        elif amount > balance:
            print("Insufficient funds!")
        else:
            print("Invalid amount! Please enter a positive number.")

    # Check balance
    elif choice == "3":
        print(f"Your current balance is: ${balance:.2f}")

    # Exit the program
    elif choice == "4":
        print("Thank you for using Your Bank. Goodbye!")
        break

    # Invalid input
    else:
        print("Invalid choice! Please select a valid option.")
