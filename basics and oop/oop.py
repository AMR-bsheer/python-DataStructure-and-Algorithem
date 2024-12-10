# basic concepts in oop
# 1.objects
# 2.classes
# 3.inheritance
# 4.polymorphism


# Example
# تعريف الفئة
class Car:
    # دالة المُنشئ __init__ it called constructor
    def __init__(self, brand, model, year): # self is a refrence to the current object
        self.brand = brand  # خاصية العلامة التجارية
        self.model = model  # خاصية الطراز
        self.year = year    # خاصية سنة التصنيع
    
    # تعريف دالة داخل الفئة method that print information about cars
    def display_info(self):
        print(f"السيارة {self.brand} - الطراز {self.model} - سنة الصنع {self.year}")
# إنشاء كائنات من فئة Car
car1 = Car("Toyota", "Corolla", 2020)
car2 = Car("Ford", "Mustang", 2022)

# استخدام الدالة display_info
car1.display_info()  # سيعرض معلومات السيارة الأولى
car2.display_info()  # سيعرض معلومات السيارة الثانية


# inhritance
# تعريف فئة ElectricCar ترث من Car
class ElectricCar(Car):
    def __init__(self, brand, model, year, battery_capacity):
        # استدعاء دالة المُنشئ للفئة الأم
        super().__init__(brand, model, year)
        self.battery_capacity = battery_capacity  # خاصية إضافية
    
    # دالة جديدة لفئة ElectricCar
    def display_battery_info(self):
        print(f"سعة البطارية: {self.battery_capacity} كيلو واط/ساعة")

# إنشاء كائن من ElectricCar
electric_car = ElectricCar("Tesla", "Model S", 2023, 100)
electric_car.display_info()            # استدعاء دالة من الفئة الأم
electric_car.display_battery_info()    # استدعاء دالة خاصة بالفئة الابنة


# polymorphism
class Animal:
    def sound(self):
        print("بعض الحيوانات تصدر أصوات")

class Dog(Animal):
    def sound(self):
        print("الكلب ينبح")

class Cat(Animal):
    def sound(self):
        print("القط يموء")

# أمثلة
animals = [Dog(), Cat()]

for animal in animals:
    animal.sound()  # سيطبع الصوت المناسب لكل حيوان

# شرح self

class Person:
    def __init__(self, name, age):
        self.name = name  # نربط الاسم بالكائن باستخدام self
        self.age = age    # نربط العمر بالكائن باستخدام self
    
    def greet(self):
        print(f"مرحبا، اسمي {self.name} وعمري {self.age} سنوات.")



# example from lecture

class Course :
    def __init__(self, name , course_id , credits):
        self.name = name 
        self.course_id = course_id
        self.credits= credits

    def display_info(self):
        print(f"Name:{self.name} , Course ID : {self.course} , Credits : {self.credits}")

# create object 
course = Course("Amr", 101 , 50)

Course.display_info()


# Encapsulation an Acess control 

class Student:
    def __init__(self,name , student_id):
        self.__name = name # private attribute 
        self.__student_id = student_id # private attribute
    
    def display_student_info(self):
        print(f"Name : {self.name} , Student ID : {self.__student_id}")

# create object 
student = Student("Mohamed" , 102)

Student.display_student_info()



# inheritance 

# define a base person class
class Person :
    def __init__(self , name ):
        self.name = name 
    
    def greet(self):
        print(f"Name : {self.name}")

# Define an Instructor class that inherits from Person
class Instructor(Person):
    def __init__(self, name, instructor_id):
        super().__init__(name) # Call the constructor of the base class
        self.instructor_id = instructor_id

    def display_instructor_info(self):
        print(f"Instructor Name: {self.name}, Instructor ID: {self.instructor_id}")

# Create an Instructor object
instructor = Instructor("Dr. Smith", 5001)
instructor.greet()
instructor.display_instructor_info()


# polymorphism

# define a base class user 
class User :
    def login (self):
        print("user logged in")

# define a subclass student with its own implementation of login
class Student(User):
    def login (self):
        print("student logged in ")

# Define a subclass Instructor with its own implementation of login
class Instructor(User):
    def login (self):
        print("Instructor logged in ")

# Polymorphic behavior
users = [Student() , Instructor()]
for user in users:
    user.login
