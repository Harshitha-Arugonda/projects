print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

#Write your code below this line 👇
c=input('you\'re at a crossroad where do you want to go? type "right" or "left": ').lower()
if c == "right":
  print("GAME OVER")
elif c=="left":
  c1=input('you have reached a lake. There is a island in the middle of the lake. Type "wait" to wait for a boat or "swim" to swim across: ').lower()
  if c1=="swim":
    print("you have drowned!! GAME OVER")
  elif c1=="wait":
    c2=input('you have reached the island unharmed. There is a house with three doors "red" and "blue" and "yellow" select any one of them: ').lower()
    if c2=="red":
      print("you have entered a romm of fire!!! GAME OVER")
    elif c2=="blue":
      print("you fell into a hole!!! GAME OVER")
    elif c2=="yellow":
      print("YOU WON!!!")
    else:
      print("you chose a door that doesnt exist")
  else:
    print("you got attacked!!! GAME OVER")
else:
  print("you fell into a hole")
              
    
