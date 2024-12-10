class person :
    def __init__(self,name,age):#proparties of class
        self.name=name
        self.age=age
    # function 
    def greet (self):
        print(f"hello {self.name}")
# createing objects
person1=person("amr",18)
person2=person("aser",19)
# use object and function
person1.greet()
person2.greet()

# new class inhreit from last class
class student(person):
    def __init__(self,name,age,student_id):#proparties
        super().__init__(name , age )
        self.student_id=student_id
    # function
    def display_info(self):
        print(f"name:{self.name} age:{self.age} id:{self.student_id}")
# creating objects
student1=student("mahmoud",18,100)
student2=student("omar",17,150)

student1.display_info()
student2.display_info()