# Initialize balance
balance = 0.0

# Function to display the menu
def show_menu():
    print("\nWelcome to Your Bank!")
    print("1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

# Function to deposit money
def deposit():
    global balance
    amount = float(input("Enter amount to deposit: "))
    if amount > 0:
        balance += amount
        print(f"Deposited successfully! New balance: ${balance:.2f}")
    else:
        print("Invalid amount! Please enter a positive number.")

# Function to withdraw money
def withdraw():
    global balance
    amount = float(input("Enter amount to withdraw: "))
    if amount > 0 and amount <= balance:
        balance -= amount
        print(f"Withdrawal successful! New balance: ${balance:.2f}")
    elif amount > balance:
        print("Insufficient funds!")
    else:
        print("Invalid amount! Please enter a positive number.")

# Function to check balance
def check_balance():
    print(f"Your current balance is: ${balance:.2f}")

# Main program loop
while True:
    show_menu()
    choice = input("Choose an option (1-4): ")

    if choice == "1":
        deposit()
    elif choice == "2":
        withdraw()
    elif choice == "3":
        check_balance()
    elif choice == "4":
        print("Thank you for using Your Bank. Goodbye!")
        break
    else:
        print("Invalid choice! Please select a valid option.")
