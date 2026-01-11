#Method :
# A method is a function that is defined inside a class and is used to perform operations using the attributes of that class.
# Methods are similar to functions, but they are associated with a specific class and can access its attributes and behaviors.

#type of methods :
#1. Instance Methods
#2. Class Methods
#3. Static Methods

#1. Instance Methods : Instance methods are the most common type of methods in Python classes.
#intstance methods are used when we want to perform operations that are related to a specific instance of a class.


class Student:
      course = 'data science'  #class attribute
      institute = 'The kiran academy'
      trainer = 'Vaibhav Patil'
      def __init__(self,nm,ag,rl):
            self.name = nm
            self.age = ag
            self.rollno = rl
            self.marks = {}
      def details(self):
            data = f'''
            Institute Name : {Student.institute}
            Name : {self.name}
            Age : {self.age}
            Roll No : {self.rollno}
            '''
      def add_marks(self,sub,marks):
            self.marks[sub] = marks
            return 'done'
      
      def show_marks(self):
            for sub,marks in self.marks.items():
                  print(f'{sub} : {self.marks[sub]}')
      
      def percentage(self):
            total_marks = sum(self.marks.values())
            percentage = (total_marks / (len(self.marks)*100)) * 100
            return percentage
      
      def check_result(self):
            if self.percentage() >= 40:
                  return 'pass'
            else:
                  return 'fail'
      def get_course_details(self):
            return f'Course Name : {Student.course}\nTrainer Name : {Student.trainer}'    

s1 = Student("Alice",20,101)
s2 = Student("Bob",22,102)
print(s1.add_marks('Python',80))
print(s1.add_marks('ML',70))
print("________________________________________________________________________________________________________________________________________")

s1.show_marks()
print(s1.percentage())
print(Student.check_result(s1))
print(s1.get_course_details())
print("________________________________________________________________________________________________________________________________________")
#class methods : Class methods are methods that are bound to the class and not the instance of the class.
#They
#are defined using the @classmethod decorator and take cls as the first parameter instead of self.
#why use class methods : Class methods are used when we want to perform operations that are related to the class itself rather than a specific instance of the class.
class Animal:
      species = 'Mammal'
      
      @classmethod
      def get_species(cls):
            return f'Species : {cls.species}'
      
      @classmethod
      def set_species(cls,spc):
            cls.species = spc
            return 'Species updated successfully'
      
print(Animal.get_species())
print(Animal.set_species('Reptile'))


print("________________________________________________________________________________________________________________________________________")


#static methods : Static methods are methods that do not depend on the instance or class of the class.
#They are defined using the @staticmethod decorator and do not take self or cls as the first parameter.
#why use static methods : Static methods are used when we want to perform operations that are related to the class but do not require access to the instance or class attributes.

class Math:
      @staticmethod
      def add(n1,n2):
            return n1 + n2
      
      @staticmethod
      def multiply(n1,n2):
            return n1 * n2
print(Math.add(10,20))
print(Math.multiply(10,20))

#Summary :
#1. Instance methods are used to perform operations related to a specific instance of a class.
#2. Class methods are used to perform operations related to the class itself.
#3. Static methods are used to perform operations that do not require access to the instance or class attributes.


#if didnt apply decorators on static method then we have to pass any parameter while calling the method
class Math:
      def add(n1,n2):
            return n1 + n2
      
      def multiply(n1,n2):
            return n1 * n2
print(Math.add(10,20))
print(Math.multiply(10,20))
print("________________________________________________________________________________________________________________________________________")     