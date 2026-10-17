
import random

secret_number = random.randint(1, 10)
#print(secret_number)  # For testing purposes, you can remove this line in production

while True:
    guess = int(input("Guess a number between 1 and 10: "))

    if guess < secret_number:
        print("Too low! Try again.")
    elif guess > secret_number:
        print("Too high! Try again.")
    else:
        print("Congratulations! You guessed the correct number.")
        print(f"The secret number is: {secret_number}")
        break
