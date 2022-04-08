import random
rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

#Write your code below this line 👇
userChoice = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors. :"))
if userChoice < 0 or userChoice >= 3:
  print("Please choose between 0 - 1 or 2 ")
else:
  if userChoice == 0:
    print(f"You chose Rock {rock}")
  elif userChoice == 1:
    print(f"You chose Paper {paper}")
  elif userChoice == 2:
    print(f"You chose scissors {scissors}")

  computer_choice = random.randint(0, 2)
  if computer_choice == 0:
    print(f"Computer chose Rock {rock}")
  elif computer_choice == 1:
    print(f"Computer chose Paper {paper}")
  elif computer_choice == 2:
    print(f"Computer chose scissors {scissors}")

  if userChoice == 0 and computer_choice == 2:
    print("You win!")
  elif userChoice == 1 and computer_choice == 0:
    print("You win!")
  elif userChoice == 2 and computer_choice == 1:
    print("You win!")
  elif userChoice == computer_choice:
    print("Equality")
  else:
    print("You lose")