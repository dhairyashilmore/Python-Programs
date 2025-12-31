#create a function to cal selling price after discount
def cal_selling_price(price, dis):
      dp = price *dis/100
      sp = price - dp
      print(sp)

cal_selling_price(1000,10)

#create a function to cal simlpe interest
def cal_simple_interest(p, r, t):
      si = (p * r * t)/100
      print(si)
cal_simple_interest(100000,12.5,1)


#Types of Arguments
#1.Positional Arguments : It is Value passed into function in correct positional order
#wrong positional order

    #def function(p1,p2)
    #function(v1,v2)

#Eg. 

def student_info(name, age, course,institude):
      data = f"Name: {name} \nAge: {age} \nCourse: {course} \nInstitude: {institude}"
      print(data)

student_info("John", 22, "MCA", "XYZ")


#2. Keyword Arguments : It is Value passed into function with key and value pair
    #def function(p1,p2)
    #function(p2=v2,p1=v1)

#Eg. 
def student_info(name, age, course,institude):
      data = f"Name: {name} \nAge: {age} \nCourse: {course} \nInstitude: {institude}"
      print(data)
student_info(course="MCA", name="John", institude="XYZ", age=22)

#3.Defualt argument : It is Uses Default value that passed on while creating object. 


#Practice Examples

#1.Write a program even or not
def even_odd(num):
      if num % 2 == 0:
            return True
      else:
            return False
print(even_odd(5))


#2.Write a program to check result pass or fail

def result(marks):
      if marks >=40:
            return "Pass"
      else:
            return "Fail"
      
print(result(50))


#3. create a function to cal percentage 

def per(Tm,Om):
      per = (Om/Tm)*100

      return per

print(per(800,596))
      

#4.create a fun to reverse and word
def rev(word):
      rev = ''
      n = len(word)
      for i in range(n-1,-1,-1):
            rev += word[i]
      return rev


print(rev("vaibhav"))


def count_char(word,char):
      count = 0
      for i in word:
            if i == char:
                  count += 1
      return count

print(count_char("Dhairyashil","a"))


def kmi(km):
      m = km * 1000
      return m
print(kmi(2))


#Nestted Function 


def f1():
      print("Inside f1")
      def f2():
            print("Inside f2")
      return f2
fun = f1()
fun()  #calling f2