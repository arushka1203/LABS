 #1
 
number = int(input())

   thousands = number // 1000
  hundreds = (number // 100) % 10
 tens = (number // 10) % 10
 units = number % 10

 if thousands + units == abs(tens - hundreds):
     print("YES")
 else:
     print("NO") 
 
#2
 age = int(input("Возраст: "))
if age >= 18:
    print("Доступ разрешен")
else:
    print("Доступ запрещен")

#3

 a = int(input())
b = int(input())
c = int(input())

if b - a == c - b:
    print("ДА")
else:
    print("НЕТ")



  #4
 x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

if x1 == x2 or y1 == y2:
    print("ДА")
else:
    print("НЕТ")

 
 #5

 y1 = int(input())
y2 = int(input())
x2 = int(input())
y2 = int(input())

if abs(x1 - x2) <= 1 and abs(y1 - y2) <= 1:
    print("YES")
else:
    print("NO")


 #6

 a = int(input())
b = int(input())
c = int(input())

if a > b:
    if a > c:
        if b > c:
            average = b
        else:
            average = c
    else:
        average = a
else:
    if b > c:
        if a > c:
            average = a
        else:
            average = c
    else:
        average = b

print(average)




 #7

month = int(input())

days = 31

if month == 4 or month == 6 or month == 9 or month == 11:
    days = 30

if month == 2:
    days = 28

print(days)




 #8
 weight = int(input())
category = ""

if weight <= 60:
    category = "Light weight"
else:
    if weight <= 64:
        category = "First welterweight"
    else:
        if weight <= 69:
            category = "Welterweight"

print(category)


 


 #9

 password = input()
 confirmation = input()

 if password == confirmation:
     print("Password accepted")
 else:
     print("Password not accepted")



 #10
 number = int(input("Enter an integer: "))

 if number % 2 == 0:
     print("Even")
 else:
     print("Odd")
    


 #11

 num1 = int(input("Enter the first integer: "))
 num2 = int(input("Enter the second integer: "))

 if num1 < num2:
     smallest = num1
 else:
     smallest = num2

 print("The smallest number is:", smallest)


 #12
 age = int(input("Enter your age: "))


 if age <= 13:
     age_group = "childhood"
 else:
     if age <= 24:
         age_group = "youth"
     else:
         if age <= 59:
             age_group = "maturity"
         else:
             age_group = "old age"

 print("You belong to the age group:", age_group)



 #13

side1 = int(input("Enter the length of the first side: "))
side2 = int(input("Enter the length of the second side: "))
side3 = int(input("Enter the length of the third side: "))


if side1 == side2 == side3:
    triangle_type = "Equilateral"
else:
    if side1 == side2 or side1 == side3 or side2 == side3:
        triangle_type = "Isosceles"
    else:
        triangle_type = "Versatile"

print("The triangle is:", triangle_type)