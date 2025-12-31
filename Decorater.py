#Decoraters in Python 
 #decorater is a function that takes another function as an argument , 
 # extends its behavior without explicitly modifying it.



def deco(fun):
      def inner():
            fun()
            print('Welcome')
            print('welcome')
            print('welcome')
            print('welcome')
      return inner



@deco
def printer():
      print('welcome')
      print('welcome')
printer()


#2
def deco(fun):
      def inner():
            result = fun()
            n3 =  int(input("Enter third number : "))
            return result + n3
      return inner

@deco
def sum_2():
      n1 = int(input("Enter first number : "))
      n2 = int(input("Enter Second number :"))
      return n1+n2
print(sum_2())


#3
def upper_deco(fun):
      def inner():
            str1 = fun()
            return str1.upper()
      return inner
@upper_deco
def greet():
      return 'good morning'

print(greet())