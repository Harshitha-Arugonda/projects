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

game_images = [rock, paper, scissors]
comp_choice=random.randint(0,2)
user_choice=int(input("enter 0 for rock, 1 for paper and 2 for scissors"))
print("you chose:")
print(game_images[user_choice])
print("Computer chose:")
print(game_images[comp_choice])

if user_choice >= 3 or user_choice < 0: 
  print("You typed an invalid number, you lose!") 
elif user_choice == 0 and comp_choice == 2:
  print("You win!")
elif comp_choice == 0 and user_choice == 2:
  print("You lose")
elif comp_choice > user_choice:
  print("You lose")
elif user_choice > comp_choice:
  print("You win!")
elif comp_choice == user_choice:
  print("It's a draw")
  
