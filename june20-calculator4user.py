def add(a, b): return a + b
def subtract(a, b): return a - b
def multiply(a, b): return a * b
def divide(a, b): return a / b if b != 0 else "Cannot divide by zero"

# Get user input
num1 = float(input("Enter the first number: "))
op = input("Enter an operation (+, -, *, /): ")
num2 = float(input("Enter the second number: "))

# Perform the chosen operation
if op == "+":
    result = add(num1, num2)
elif op == "-":
    result = subtract(num1, num2)
elif op == "*":
    result = multiply(num1, num2)
elif op == "/":
    result = divide(num1, num2)
else:
    result = "Invalid operation"

print("Result:", result)