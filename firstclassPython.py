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

for num in range(1, 1001):
    print(num)


def is_prime(n):
    if n < 2:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# Testing the function
number = int(input("Enter a number: "))
if is_prime(number):
    print(f"{number} is a prime number.")
else:
    print(f"{number} is not a prime number.")

print("Prime numbers from 1 to 100:")
for num in range(1, 101):
    if is_prime(num):
        print(num, end=" ")

n = int(input("Enter how many Fibonacci numbers to print: "))
a = 0
b = 1
for i in range(n):
   print(a)
   next = a + b
   a = b
   b = next        



        