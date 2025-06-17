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