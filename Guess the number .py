import random

print("Welcome to the number game. A random number will be generated and you can guess which one it is.")
print("You got three tries.")

number = random.randint(1, 99)
guess = ""  # var to store users guess
guess_count = 0
guess_limit = 3
out_of_guesses = False

while guess != number and not out_of_guesses:
    if guess_count < guess_limit:
        guess = int(input("Enter a guess: "))
        guess_count += 1
        if guess < number:
            print("Your guess is too small. Try again.")
        elif guess > number:
            print("Your guess is too high. Try again.")
    else:
        out_of_guesses = True

if out_of_guesses:
    print("You are out of guesses. You loose!")
else:
    print("Your guess is correct. You Won!")