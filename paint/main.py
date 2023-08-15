import math 
def paint(height,width,coverage):
  area=height*width
  #math.ceil rounds of the decimal to nxt no, import math to use this fn
  cans=math.ceil(area/coverage) 
  print(f"you will need {cans} cans of paint")
x=int(input("enter height of the wall"))
y=int(input("enter width of the wall"))
paint(x,y,5)