# class student:
#       def __init__(self,name,age):
#             self.__name = name
#             self.__age = age
#       def getname(self):
#             return self.__name
#       def getage(self):
#             return self.__age
#       def set_name(self,nm):
#             self.__name = nm
#       def set_age(self,ag):
#             if ag> 0 and ag<120:
#                     self.__age = ag  
#             else:
#                   print("Invalid age value")    


# s1 = student('vaibhav',21)  

# print(s1.getage())
# s1.set_name('Kiran')
# print(s1.getname())     
# # print(s1.name)
# s1.age = 300
# print(s1.age)

# class counter:
#       def __init__(self):
#             self.count = 0 #public : Anyone can access this attributes outside the class
#       def inc(Self):
#             Self.count+=1 #we can it private using "__" double underscore but use this only inside the class
#       def dec(self):
#             self.count -= 1
#       def check(self):
#             return self.count
      
# d = counter()
# d.inc()
# d.inc()
# d.inc()

# print(d.check())
# print(d.count)

# #--------------------------------------------------------------------------------------------------

# class counter:
#       def __init__(self):
#             self.__count = 0 #public : Anyone can access this attributes outside the class
#       def inc(Self):
#             Self.__count+=1 #we can it private using "__" double underscore but use this only inside the class
#       def dec(self):
#             self.__count -= 1
#       def check(self):
#             return self.__count
      
# d = counter()
# d.inc()
# d.inc()
# d.inc()

# print(d.check())
# print(d.count)



class Students:
    def __init__(self, nm, ag):
        self.__name = nm   # private
        self.__age = ag    # private

    def getname(self):
        return self.__name

    def getage(self):
        return self.__age
    
    def set_name(self,nm):
        if isinstance(nm,str):
            self.__name = nm
        else:
            print("Invalid name")

    def set_age(self,ag):
        if isinstance(ag,(int,float)) and ag>0 and ag<100:
            self.__age = ag
        else:
            print("Invalid age value")
      
         


s = Students("Dhairyashil", 22)
print(s.getname())
print(s.getage())
s.set_name("om patil")
print(s.getname())

