print("Hello World!")
print([1,2,3,4,5,6,7,8,9,10])

name = input("What is your name? ")
print("Hello, " + name + "!")

a = int(input("Enter first number: "))
b = int(input("Enter second number: "))
print("Sum is:", a + b)

for i in range(1, 11):
    print(i)
a = 5
b = 10
c = 3
print("Largest is", max(a, b, c))

num = int(input("Enter a number: "))
if num % 2 == 0:
    print("Even")
else:
    print("Odd")

    num = int(input("Enter a number: "))
if num % 5 == 0:
    print("you're free to")
else:
    print("sorry, you stay in prison")

import random
print("Random number:", random.randint(1, 100))


print(" Welcome to the Guessing Game!")
secret_number = random.randint(1, 10)
attempts = 3
 
while attempts > 0:
    guess = int(input("Guess a number between 1 and 10: "))
    if guess == secret_number:
        print("🎉 Correct! You win!")
        break
    else:
        attempts -= 1
        if guess < secret_number:
            print("Too low!")
        else:
            print("Too high!")
 
        if attempts > 0:
            print(f"Try again! {attempts} attempts left.")
        else:
            print(f" Out of tries! The number was {secret_number}.")

    # Asking for user input
name = input("What is your name? ")
age = input("How old are you? ")

# Displaying the result
print(f"Hello, {name}! You are {age} years old.")

# Asking for user input
name = input("What is your name? ")
print(f"Thank you, {name}!")

job = input("What is your job? ")
salary = input("What is your salary? ")
location = input("Where are you located? ")

# Displaying the final message
print(f"I, {name}, from {location}, working as a {job}, with the salary of {salary}, would love to work in cloud and AI.")



        