class Student:
      def __init__(self):
            print("This is Student class")

      def display(self):
            print("This is display method of Student class" )
s1 = Student()
s2 = Student()



#constructor : is a special method that is automatically called when an object of a class is created.
# In Python, the constructor method is defined using the __init__() method.
# The primary purpose of a constructor is to initialize the attributes of the object and allocate any necessary resources.

class Student:
      def __init__(self):
            print(f'id of self is {id(self)}')
s1 = Student()
print(f'id of s1 is {id(s1)}')
s2 = Student()
print(f'id of s2 is {id(s2)}')


#Example 2 
#Type of Attributes 
#1. Instance Attributes
#2. Class & Static Attributes
#3. Dynamic Attributes

#1`. Instance Attributes : instance attributes are defined inside the constructor using the self parameter.

class Student:
      def __init__(self,nm,ag,ct):
            self.name = nm #instance attribute
            self.age = ag  #instance attribute
            self.city = ct #instance attribute
s1=Student("Alice",20,"New York")
print(s1.name,s1.age,s1.city)

s2=Student("Bob",22,"Los Angeles")
print(s2.name,s2.age,s2.city)

#2. Class & Static Attributes : Class attributes are defined within the class but outside any methods.
# They are shared among all instances of the class.   

class Student:
      institute = 'The kiran academy'  #class attribute
      trainer = 'Vaibhav Patil'
      course = 'data science'
      def __init__(self,nm,ag,ct):
            self.name = nm          #instance attribute
            self.age = ag           #instance attribute
            self.city = ct          #instance attribute
s1=Student("Alice",20,"New York")
print(s1.name)
print(s1.age)
print(s1.city)
print(Student.institute)
print(Student.trainer)


#Revison Example

class Student: 
      