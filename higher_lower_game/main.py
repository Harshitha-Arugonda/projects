from game_data import data
import random
from art import logo, vs
from replit import clear

def random_number():
  return random.choice(data)
def data_info(account):
  name = account["name"]
  description = account["description"]
  country = account["country"]
  return f"{name}, a {description}, from {country}"

def check_answer(guess,a_followers,b_followers):
  if a_followers > b_followers:
    return guess == "a"
  else:
    return guess == "b"

def game():
  print(logo)
  score=0
  should_continue=True
  account_a = random_number()
  account_b = random_number()

  while should_continue:
    account_a = account_b
    account_b = random_number()

    while account_a == account_b:
      account_b = random_number()
    
    print(f"Compare A: {data_info(account_a)}.")
    print(vs)
    print(f"Against B: {data_info(account_b)}.")
    
    guess=input("guess who has more followers??? type 'A' or 'B' ").lower()
    a_follower_count = account_a["follower_count"]
    b_follower_count = account_b["follower_count"]
    is_correct = check_answer(guess, a_follower_count, b_follower_count)
    clear()
    print(logo)
    if is_correct:
      score += 1
      print(f"You're right! Current score: {score}.")
    else:
      should_continue = False
      print(f"Sorry, that's wrong. Final score: {score}")

game()
  
    
  