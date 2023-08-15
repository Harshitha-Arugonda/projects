# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ").upper()
add_pepperoni = input("Do you want pepperoni? Y or N ").upper()
extra_cheese = input("Do you want extra cheese? Y or N ").upper()
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
if size == "S":
  if add_pepperoni == "Y" and extra_cheese =="Y":
    print("your bill is $18")
  elif add_pepperoni == "Y" and extra_cheese =="N":
    print("your bill is $17")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print("your bill is $16")
  else:
    print("your bill is $15")
elif size == "M":
  if add_pepperoni == "Y" and extra_cheese =="Y":
    print("your bill is $24")
  elif add_pepperoni == "Y" and extra_cheese == "N":
    print("your bill is $23")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print("your bill is $21")
  else:
    print("your bill is $20")
elif size == "L":
  if add_pepperoni == "Y" and extra_cheese =="Y":
    print("your bill is $29")
  elif add_pepperoni == "Y" and extra_cheese == "N":
    print("your bill is $28")
  elif add_pepperoni == "N" and extra_cheese == "Y":
    print("your bill is $26")
  else:
    print("your bill is $25")
  


