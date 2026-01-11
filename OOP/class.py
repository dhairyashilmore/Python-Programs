#Using List to store : create student details

#student details
Student_1 = ['Madhav',10]
Student_2 = ['Kiran',12]

print(f'Student Name : {Student_1[0]}')
print(f'Student Age : {Student_1[1]}')


#type of attributes :
#1. Instance Attributes : Instance attributes are the attributes that are specific to each instance of a
#class. They are defined inside the __init__ method and are prefixed with self.
#2. Class Attributes : Class attributes are the attributes that are shared by all instances of a class. They are defined outside the __init__ method and are prefixed with the class name.

class Student:
      #class attributes
      institute = 'The Kiran Academy'
      course = 'MCA'
      
      def __init__(self,nm,ag,rl):
            #instance attributes
            self.name = nm
            self.age = ag
            self.rollno = rl

s1 = Student('Vaibhav',21,101)


#Ex.1

import math
class cirlce:
      def __init__(self,radius):
            self.radius = radius 
      
      def area(self):
            return math.pi *(self.radius **2)
      def circum(self):
            return 2*math.pi*self.radius
      

rad  = 45
r1 = cirlce(rad)
print("Area of circle :", r1.area())


#Ex.2

class student:
      def __init__(self,nm,ag,gd):
            self.name = nm
            self.age = ag
            self.gd = gd

      def details(self):
            return f''' 
            Name : {self.name}
            Age : {self.age}
            GD : {self.gd}

            '''

s1 = student('kiran',21,'M')
print(s1.details())      
      

#EX.3

class student:
      pass


s1 = student()



#ex.4


      