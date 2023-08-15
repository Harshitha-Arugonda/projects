from replit import clear
logo = """
 _____________________
|  _________________  |
| | calculator   0. | |  .----------------.  .----------------.  .----------------.  .----------------. 
| |_________________| | | .--------------. || .--------------. || .--------------. || .--------------. |
|  ___ ___ ___   ___  | | |     ______   | || |      __      | || |   _____      | || |     ______   | |
| | 7 | 8 | 9 | | + | | | |   .' ___  |  | || |     /  \     | || |  |_   _|     | || |   .' ___  |  | |
| |___|___|___| |___| | | |  / .'   \_|  | || |    / /\ \    | || |    | |       | || |  / .'   \_|  | |
| | 4 | 5 | 6 | | - | | | |  | |         | || |   / ____ \   | || |    | |   _   | || |  | |         | |
| |___|___|___| |___| | | |  \ `.___.'\  | || | _/ /    \ \_ | || |   _| |__/ |  | || |  \ `.___.'\  | |
| | 1 | 2 | 3 | | x | | | |   `._____.'  | || ||____|  |____|| || |  |________|  | || |   `._____.'  | |
| |___|___|___| |___| | | |              | || |              | || |              | || |              | |
| | . | 0 | = | | / | | | '--------------' || '--------------' || '--------------' || '--------------' |
| |___|___|___| |___| |  '----------------'  '----------------'  '----------------'  '----------------' 
|_____________________|
"""
print(logo)
def add(n1,n2):
  return n1+n2
def sub(n1,n2):
  return n1-n2
def multiply(n1,n2):
  return n1*n2
def divide(n1,n2):
  return n1/n2
def modulus(n1,n2):
  return n1%n2
def exponent(n1,n2):
  return n1**n2
def floor_division(n1,n2):
  return n1//n2


def screen(n1,op,n2):
  if op=="+":
    x=(add(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="-":
    x=(sub(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="*":
    x=(multiply(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="/":
    x=(divide(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="%":
    x=(modulus(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="**":
    x=(exponent(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  elif op=="//":
    x=(floor_division(n1,n2))
    print(f"{n1}{op}{n2}={x}")
  Y=input("type 'y' to continue calculating or 'n' to start a new calculation ")
  if Y=="y":
    n1=x
    print("the first number is",n1)
    op=input("enter the operator")
    n2=int(input("enter the next number"))
    screen(x,op,n2)
  elif Y=="n":
    clear()
    n1=int(input("enter the first number"))
    op=input("enter the operator")
    n2=int(input("enter the next number"))
    screen(n1,op,n2)
n1=int(input("enter the first number"))
op=input("enter the operator")
n2=int(input("enter the next number"))
screen(n1,op,n2)
  

