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

s1 = Student("Alice",20,101)
s2 = Student("Bob",22,102)
print(s1.add_marks('Python',95))
print(s1.add_marks('ML',90))
print(s1.add_marks('DS',85))
s1.show_marks()
s1.percentage()
print(f'Percentage of {s1.name} is {s1.percentage()}%')
