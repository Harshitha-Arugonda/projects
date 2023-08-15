import random
# Split string method
names_string = input("Give me everybody's names,separated by a comma. ")
names = names_string.split(",")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
x=len(names)
random_choice=random.randint(0,x-1)
p=names[random_choice]
print(p + " is going to buy the meal today")


