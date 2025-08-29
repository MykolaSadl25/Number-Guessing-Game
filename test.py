

import time

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Go!")

phonebook = {"Alice": "123", "Bob": "456"}
print(phonebook["Alice"])   # 123
phonebook["Charlie"] = "789" # add a new entry

import random
print(random.randint(1, 10))  # random integer 1 to 10
print(random.choice(['rock', 'paper', 'scissors'])) # pick random element

# Simple calculator
num1 = float(input("Enter first number: "))
op = input("Enter operator (+, -, *, /): ")
num2 = float(input("Enter second number: "))

if op == "+":
    print("Result:", num1 + num2)
elif op == "-":
    print("Result:", num1 - num2)
elif op == "*":
    print("Result:", num1 * num2)
elif op == "/":
    if num2 != 0:
        print("Result:", num1 / num2)
    else:
        print("Error: Division by zero")
else:
    print("Invalid operator")

