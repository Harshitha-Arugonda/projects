from replit import clear
import random
def repeat():
  b=input("type 'y' to get another card and 'n' to pass")
  if b=="n":
    print("your final hand:",s)
    s1.append(random.choice(cards))
    print("computer's final hand:",s1)
  elif b=="y":
    s.append(random.choice(cards))
    print("your final cards:",s)
    s1.append(random.choice(cards))
    print("computer's final hand:",s1)

a=input("do you want to play a game of blackjack? if yes type 'y' and 'n' for no:")
if a=="n":
   clear()
if a=="y":
  clear()
  logo = """
.------.            _     _            _    _            _    
|A_  _ |.          | |   | |          | |  (_)          | |   
|( \/ ).-----.     | |__ | | __ _  ___| | ___  __ _  ___| | __
| \  /|K /\  |     | '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
|  \/ | /  \ |     | |_) | | (_| | (__|   <| | (_| | (__|   < 
`-----| \  / |     |_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
      |  \/ K|                            _/ |                
      `------'                           |__/           
"""
  print(logo)
  cards=[11,2,3,4,5,6,7,8,9,10,10,10,10]
  s=random.sample(cards,2)
  print("your cards:",s)
  s1=random.sample(cards,1)
  print("computer's first card",s1)
  repeat()
  first=sum(s)
  second=sum(s1)
  if first>second and first<21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("you win 🥳")
  elif first<second and second<21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("you lose 😢")
  elif first>21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("bust,you lost 😭")
  elif second>21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("you win,computer busted 🤩")
  elif first==21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("it's a blackjack,you won 😎")
  elif second==21:
    print("your total sum:",first)
    print("computer's total sum:",second)
    print("computer got a blackjack,you lost 😱")
  
    

 


