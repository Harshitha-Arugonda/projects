# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆
height=sum(student_heights)
no_of_students=len(student_heights)
avg=height/no_of_students
x=round(avg,2)
print(f"the avg height of given students is:{x}")

#Write your code below this row 👇
i=0
for x in student_heights:
  i+=x
m=0
for y in student_heights:
  m+=1
z=round(i/m,2)
print(f"the avg height of given students is:{z}")




