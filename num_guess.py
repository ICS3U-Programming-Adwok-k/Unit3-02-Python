#!/usr/bin/env python3
# Created by: Adowk Adiebo
# Created on: March 19th, 2025
# This program asks you to guess the correct
# number.
import constants

def main():
    # This code is asking for the guessed number
    guessed_number = int(input("Guess the correct number: "))

    # Enter the guessed number
    if guessed_number == constants.CORRECT_NUMBER:
        print("You guessed correctly!")
        print("")
        print("Congratulations.")

    # Enter the Guessed number
    if guessed_number != constants.CORRECT_NUMBER:
        print("You guessed wrong.")
        print("")
        print("Please try again.")


if __name__ == "__main__":
    main()
