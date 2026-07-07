"""
Number Guessing Game
The computer picks a random number, and you try to guess it
within a limited number of attempts, with hints along the way.
"""

import random


def play_round(min_num=1, max_num=100, max_attempts=7):
    secret = random.randint(min_num, max_num)
    attempts = 0

    print(f"\nI'm thinking of a number between {min_num} and {max_num}.")
    print(f"You have {max_attempts} attempts. Good luck!\n")

    while attempts < max_attempts:
        guess_input = input(f"Attempt {attempts + 1}/{max_attempts} - Your guess: ").strip()

        if not guess_input.lstrip("-").isdigit():
            print("Please enter a valid whole number.")
            continue

        guess = int(guess_input)
        attempts += 1

        if guess == secret:
            print(f"\n🎉 Correct! The number was {secret}. You got it in {attempts} attempt(s)!")
            return True
        elif guess < secret:
            print("Too low.")
        else:
            print("Too high.")

    print(f"\n💀 Out of attempts! The number was {secret}.")
    return False


def main():
    print("===== Number Guessing Game =====")
    wins = 0
    rounds = 0

    while True:
        rounds += 1
        if play_round():
            wins += 1

        print(f"\nScore: {wins}/{rounds} rounds won.")
        again = input("Play again? (y/n): ").strip().lower()
        if again != "y":
            print("Thanks for playing!")
            break


if __name__ == "__main__":
    main()
