import random

# You give a number
your_number = int(input("Enter your number (1 to 10): "))

# Computer generates a random number
computer_number = random.randint(1, 10)

print(f"You chose: {your_number}")
print(f"Computer chose: {computer_number}")

# Optional: Determine the winner
if your_number > computer_number:
    print("You win!")
elif your_number < computer_number:
    print("Computer wins!")
else:
    print("It's a tie!")