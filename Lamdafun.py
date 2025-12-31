'''
lambda function 
-A lambda function is a small anonymous function that can take any number of arguments, 
but can only have one expression. It is often used for short, 
throwaway functions that are not needed elsewhere in the code.
- It is name less function thats why its called anonoymous function

lambda paramter : expression
'''

#Eg.1
print((lambda n1,n2: n1+n2)(13,7))

#create a lambda function to cal avg of 3 number
avg = (lambda n1,n2,n3 : (n1+n2+n3)/3)(10,20,30)
print(avg)


calci = lambda n1,n2 : (n1+n2, n1-n2, n1*n2, n1/n2)
print(calci(10,5))
sum,sub,mul,div = calci(10,5)


#Higher order function

#Filter() :  


#eg

number = [10,-20,30,-40,50,60,-70,80,90,-100]
def positive(num):
      if num >=0:
            return True
      else:
            return False
print(filter(positive,number))
print(list(filter(positive,number)))

#2. 
number = [10,22,33,43,5,7,9,2,13,432]
def iseven(num):
      if num%2==0:
            return True
      else:
            return False
      
print(list(filter(iseven,number)))


#using lambda function

number = [10,22,33,43,5,7,9,2,13,432]
filter(lambda num: num%2==0,number)     

#wap to filter names starts with v 
students = ['kuna', 'vaibhav','harish','vijay','arun','varun']
print(list(filter(lambda name :  name[0]== 'v', students)))