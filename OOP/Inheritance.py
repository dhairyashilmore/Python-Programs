#Inheritance :

class xyz:
      def m1(self):
            print(" I am m1 method of XYZ class")
      def m2(self):
            print(" I am m2 method of XYZ class")

x1 = xyz()
x1.m1()

class Abc(xyz):
      def m3(self):
            print(" I am m3 method of Abc class")
      def m4(self):
            print(" I am m4 method of Abc class")


a1 = Abc()
a1.m1()
a1.m3()
a1.m4()

print("****************************************************************************************************************************")

# Bank Project using Inheritance

class Saving_account:
      bank_name = 'Bank Of Maharashtra'
      ifsc_code = 'MAHB000666'
      Branch = 'karve nagar'

      def __init__(self,nm,ac,bal):
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

      def display_details(self):
            return f'''
            Account holder name is {self.name}
            Account number is {self.account_no} 
            Available balance is {self.balance}
            Bank name is {self.bank_name}
            IFSC code is {self.ifsc_code} 
            Branch is {self.Branch}
            Account type is Saving Account
      '''
      

class current_account(Saving_account):
      def interest_rate(self):
            return super().interest_rate() + ' but current account interest rate is 3.5% p.a'

c1 = current_account('dhairyashil', 4101,30000)
c2 = Saving_account('john', 4101,40000)
print(c1.check_bal())
print(c1.display_details())
print(c2.display_details())

print("****************************************************************************************")

class Person:
    def __init__(self, name, address):
        self.name = name
        self.address = address


class Student(Person):
    def __init__(self, name, address, roll, marks):
        super().__init__(name, address)
        self.roll = roll
        self.marks = marks

    def scholarship(self):
        if self.marks >= 80:
            return "Eligible for Scholarship"
        else:
            return "Not Eligible for Scholarship"
    def display_detail(self):
         return f'''
               name : {self.name}
               Address : {self.address}
               Roll_No  : {self.roll}
               marks : {self.marks}
               '''



s1 = Student("Dhairyashil", "Pune", 101, 85)
print(s1.display_detail())
print(s1.scholarship())

print("******************************************************************")


#EX.3

class Staff:
      def __init__(self,role,dept,salary):
            self.role = role
            self.dept = dept
            self.salary = salary
      
      def details(self):
            return f'''
            name = {self.name}
            age = {self.age}
            Role = {self.role}
            dept = {self.dept}
            salary = {self.salary}

            '''

class teacher(Staff):
      def __init__(self,name,age,role,dept,salary):
            self.name = name
            self.age = age
            super().__init__(role,dept,salary)

      

      

c2 = teacher('john', 22,'prof','science',40000)
print(c2.__dict__)
      


#Ex 4


