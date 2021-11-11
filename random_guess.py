# Random guess
import random  # imports the random library

print("\n\tWelcome to the Guess your number game \n\n")

myName = input("Hello! What is your name? ")
number = random.randint(1, 10)  # random generation between 1 and 10

def main():
    guesses = 1
    print(number)
    print("Well, " + myName + " I am thinking of a number between 1 and 10.")

    while guesses < 7:
        guess = int(input("Take a guess "))
        if guess == number:
            print("Good job, " + myName + " You guesses my number")
            print("Thank you for playing")
            break
        elif guess < number:
            print("Your guess is too low.")
        elif guess > number:
            print("Your guess is too high.")
        else:
            print("Wrong, have another guess")
        guesses = guesses + 1

main()
