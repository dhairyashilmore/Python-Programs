# # Polymorphism : many forms
# # It is the ability to use a common interface for multiple forms (data types).
# # In Python, polymorphism allows methods to do different things based on the object it is acting upon.

# # n1 =10
# # n2 =20
# # print(type(n1+n2))
# # print(n1+n2)
# # print(n1.__add__(n2))
# # print(dir(n1))  #30


# class Book:
#       def __init__(self,nm, pg):
#             self.name = nm
#             self.pages = pg
#       def __add__(self,others):
#             total = self.pages+others.pages
#             return f'total number of pages : {total}'
           
# b1 = Book("Python Programming",350)
# b2 = Book("Data Science", 500)
# print(b1.__add__(b2))
# n1 = 10
# n2 = 20
# l1 = [10]
# l2 = [20]
# print(n1+n2)
# print(b1+b2)


# class Hotel:
#       def __init__(self,name,rent):
#             self.name = name
#             self.rent = rent
#       def __gt__(self,other):
#             if self.rent > other.rent:
#                   return "H1 rent is greater"
#             else:
#                   return f"H2 rent is greater"

# h1 = Hotel('taj hotel', 1000)
# h2 = Hotel('raj hotel',2000)
# print(h1>h2)


#Method overloading 


# class student: 
#       def __init__(self,nm):
#             self.name = nm
#       def __init__(self,nm,ag):
#             self.name = nm
#             self.age = ag
#       def __init__(self,nm,ag,ct):
#             self.name = nm
#             self.age = ag
#             self.city = ct
      


# s1 = student('vaibhav',21,'Pune')
# print(s1)

# Note : In python operator overloading is possible but method overloading is not possible.
# In python last defined method will be considered if there are multiple methods with same name.

# To achieve method overloading in python we can use default arguments.

#Bank Project using Polymorphism Method Overriding

#Method overriding : when a derived class has a method with same name as in its base class,

class Savinng_account:
      def __init__(self,nm,ac,bal=0):
            self.name = nm
            self.account_no = ac
            self.balance = bal
      def check_bal(self):
            return f'Availbale balance is {self.balance}'
      def deposit(self,amount):
            if amount>0:
                  self.balance +=amount
                  return 'done'
            else:
                  return 'Invalid amount value' 
      def withdraw(self,amount):
            if amount > 0:
                  if amount <= self.balance:
                        self.balance -= amount

                  else:
                        return 'Insufficient balance'
            else:
                  return 'Invalid amount value'
            
class Current_account(Savinng_account):
      ol = 5000
      def withdraw(self,amount):
            if amount +Current_account.ol <= self.balance:
                  self.balance -= amount
                  return f'withdrawn amount is {amount}'
            else:
                  return 'Insufficient balance including overdraft limit'

c2 = Current_account('vaibhav', '1234567890',22000)
print(c2.check_bal())