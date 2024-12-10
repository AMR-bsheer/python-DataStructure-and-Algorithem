# variabels
# name="amr"
# age=20
# height=1.80
# print(name , age , height)

# data type
# str => string => "amr"
# int => integer => 20
# bool => boolean => (true , false)
# float => 2.8
# type() method

# age=11
# long=2.8
# print(type(age), type(long))

# Arithmetic operators
# x=5
# y=7
# print(y+x)
# print(y-x)
# print(y/x)
# print(y*x)

# condtional statement

# x=int(input("enter your name :"))

# if x >= 18 :
#     print("adult")
# elif x >=10 and x < 18:
#     print("teen")
# else:
#     print("child")

# loops
#-----------
# for loop
# for i in range(11):
#     print(i)
#-------
#while loop
# i=0
# while i in range(0,10) :
#     i += 1
#     print(i)  


# functions
# def sum (x,y):
#     result =int(x) + int(y)
#     print("summation is"+str(result))

# sum(5 ,10)

# challenge
name=input("enter your name:")
age=int(input("enter your age:"))

if age >= 18 :
    print("hello"+" "+ name +" "+"enter numbers")
    x=int(input("enter number 1:"))
    y=int(input("enter number 2:"))
    print(f"summation is : {x+y}")
    print(f"subtraction is : {x-y}")
    print(f"multiplying is : {x*y}")
    if y == 0:
        print("you cant dividing by zero")
    else:
        print(f" dviding is :{x/y}")

else :
    print("sorry"+" "+name+" "+"you are child")

# الخطوة 4: تعريف دالة لحساب القوة
def calculate_power(base, exponent):
    return base ** exponent

# استخدام الدالة لحساب القوة
power_result = calculate_power(x , y)
print(f"{power_result}: {x}base to {y} Expnent ")
print("thank you"+" "+name)