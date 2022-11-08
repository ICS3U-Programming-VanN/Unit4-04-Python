#!/usr/bin/env python3

# Created by: Van Nguyen
# Created on: November 7, 2022
# This program asks the user to guess a generated number
# if the user guesses it wrong, the program will continue
# to ask the user to guess (this continues until the user gets it right)


import random


def main():
    # Generates random number for user to guess
    correct_number = random.randint(0, 9)

    # While-loop to repeat program until user breaks
    while True:

        # Asks user for their number guess
        user_guess_string = input("Enter your number guess (0-9): ")

        # Checks for exceptions
        try:
            # Attempts to converts user number into an integer
            user_guess = int(user_guess_string)

        # In the event of an exception
        except:
            print(f"{user_guess_string} is not a valid guess!  Try again.\n")

        # If the user entered valid input
        else:
            # If the user did not enter a number within the given range (0-9)
            if user_guess < 0 or user_guess > 9:
                print("Please enter a whole number between 0-9! Try again.\n")

            # If the user guesses the number correctly
            else:
                # If user's guess is correct
                if user_guess == correct_number:
                    print(f"You guessed correctly! The number was {correct_number}")

                    # Break out of the loop
                    break

                # If the user guessed the number incorrectly
                else:
                    print("You guessed wrong! Try again.\n")

        # Final message displayed to user regardless of input
        finally:
            print("Thank you for playing!")


if __name__ == "__main__":
    main()
