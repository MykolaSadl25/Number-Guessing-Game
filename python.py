import random

number = random.randint(1, 20)
guess = 0
attempts = 0
max_attempts = 5

print("Welcome to the guessing game!")
print(f"You have {max_attempts} attempts to guess the number between 1 and 20.")

import time

print("3...")
time.sleep(1)
print("2...")
time.sleep(1)
print("1...")
time.sleep(1)
print("Go!")

while guess != number and attempts < max_attempts:
    guess = int(input("Guess a number: "))
    attempts += 1
    remaining = max_attempts - attempts  # calculate remaining attempts

    if guess < number:
        print("Too low!")
    elif guess > number:
        print("Too high!")
    else:
        print(f"🎉 Correct! You guessed it in {attempts} tries.")

    if guess != number and remaining > 0:
        print(f"You have {remaining} attempts left.\n")
    elif remaining == 0 and guess != number:
        print(f"💥 Game over! The number was {number}. Run the game again to play")

# print("Hello, world!")

# name = "Mykola"
# age = 14

# print(type(name))
# print(type(age))

# a = 10
# b = 4

# print(a + b)   # addition → 13
# print(a - b)   # subtraction → 7
# print(a * b)   # multiplication → 30
# print(a / b)   # division → 3.333...
# print(a // b)  # floor division → 3
# print(a % b)   # remainder → 1
# print(a ** b)  # exponent → 1000

# if age>= 18:
#     print("Adult")
# else:
#     print("Little boy/girl ")


# for i in range(10):
#     print(i)