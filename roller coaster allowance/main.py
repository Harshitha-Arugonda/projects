print("welcome to the rollarcoaster")
height=float(input("enter your height in cm"))
age=int(input("enter your age"))
bill=0

if height>120:
  print("you can ride the rollar coaster")
  if age<13:
    bill=100
    print("child ticket is 100rs")
  elif age>=13 and age<=19:
    bill=200
    print("teenagers fee is 200rs ")
  elif age>=20:
    bill=300
    print("adult fee is 300rs")
  pic=input("do you want a photo if yes press y and n for no")  
  if pic=="y":
    bill+=3
    print(f"your final bill is {bill}")
  else:
    print(f"your final bill is {bill}")
else:
  print("sorry,you cannot ride the rollar coaster")