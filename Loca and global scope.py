'''
Global and Local Scope in Python
1.Global scope :   
- Space outside the function is called Global scope. 
- It can be accessed anywhere in the program. 
 
2.Local scope :
- Space inside the function is called Local scope.
- It can be accessed only inside the function.

Eg. 
x = 10  #Global Scope
y = 20
def fun():
  a = 100  #Local Scope 
  b = 200

'''

print("Global Scope in Python")
x = 20
y =30
def func():
      print("Local Scope")
      a = 100
      b = 200
      print(x,y) #We can access local scope variable within local scope
      print(a,b) #We can access global scope variable within local scope
func()



Tickets = 10
def book_ticket(name,no):
      global Tickets
      if no <= Tickets:
            print(f"{no} tickets booked successfully")
            Tickets = Tickets - no
      else:
            print("Tickets not available")
book_ticket('John',3)


'''
Return Statement in Python

- It is used to return value from function to the calling function.
Eg.
def add(a,b):
      c = a + b
      return c

Need of Return Statement
- It is used to get output from function to calling function.
- When we want result outside the function, we use return statement.
- The function give the output within a function, 
- But we want to use that output outside the function. and it in local Space
- It terminates the function execution and sends the result to the calling function. 
- After the return statement, no code will be executed within the function.

'''

def xyz(num):
      square = num**2
      return square

print(xyz(5))

