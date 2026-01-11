#arbirtray arguments : arguments which can take any number of arguments
#type of arguments : positional , keyword , arbitary , default ,  keyword arbitary   
#Purpose of arbitary arguments : when we dont know how many arguments will be passed in function
#syntax : def function_name(*args):

def sum(n1,n2):
      return n1+n2
print(sum(10,20))


def sum(*args):
      total = 0
      for n in args:
            total += n
      return total
print(sum(10,20,30,40))


from functools import reduce  
number = [1,2,3,4,5]
result = reduce(lambda sum,num: sum+num, number)
print(result)


data = ['jay','vaibhav','harish','vijay']
from functools import reduce
print((reduce(lambda full,i : full+i  + " ",data,)))

number = [1,2,3,4,5,6]
from functools import reduce
result = reduce(lambda mul,num: mul+num*num, number)
print(result)


numbers = [1, 2, 3, 4, 5]
even = list(map(lambda x: x % 2 == 0, numbers))
print(even)

numbers = [1, 2, 3, 4, 5]
even = list(filter(lambda x: x % 2 == 0, numbers))
print(even)