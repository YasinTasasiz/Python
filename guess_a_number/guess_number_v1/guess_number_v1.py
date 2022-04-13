#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

import random
from art import logo

print(logo)
print("Welcome to the Number Guessing Game!")
print("I'm thinking a number between 1 and 100.")

def difficulty_level(guess_quantity):
  number = random.randint(1, 101)
  continue_game = True
  while continue_game:
    if guess_quantity > 0:
      user_guess = int(input(f"You have {guess_quantity} attempts remaining. \nPlease guess a number : "))
      if user_guess < number:
        print("too low")
        guess_quantity -= 1
      elif user_guess > number:
        print("too high")
        guess_quantity -= 1
      else:
        print("Congratulations, you guessed the number")
        continue_game = False
    else:
      print(f"The number was {number}. You lose")
      continue_game = False

user_difficulty_choice = input("Choose a difficulty: Type 'e' for 'easy' or type 'h' for 'hard' :").lower()
if user_difficulty_choice == "e":
  difficulty_level(10)
elif user_difficulty_choice == "h":
  difficulty_level(5)
