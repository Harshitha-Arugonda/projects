import random
from replit import clear
from art import logo
print(logo)
print("welcome to the number guessing game")
print("I am thinking of a number between 1 to 100")
choice=random.choice(range(1,100))
level=input("choose a difficulty 'easy' or 'hard'")
if level=="easy":
  attempts=10
  print(f"you have {attempts} attempts remaining to guess the number ")
  guess=1
  while guess>0:
    guess=int(input("make a guess"))
    if guess>choice:
      print("too high")
      attempts-=1
    elif guess<choice:
      print("too low")
      attempts-=1
    elif guess==choice:
      print("you have got it right")
      guess=0
    if attempts==0:
      print("you are out of guesses")
      guess=0
elif level=="hard":
  attempts=5
  print(f"you have {attempts} attempts remaining to guess the number ")
  guess=1
  while guess>0:
    guess=int(input("make a guess"))
    if guess>choice:
      print("too high")
      attempts-=1
    elif guess<choice:
      print("too low")
      attempts-=1
    elif guess==choice:
      print("you have got it right")
      guess=0
    if attempts==0:
      print("you are out of guesses")
      guess=0
  