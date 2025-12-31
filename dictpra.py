# Online Python compiler (interpreter) to run Python online.
# Write Python 3 code in this online editor and run it

# #Dict Practice

# #How to access the dictionary
# ''' 1. Syntax : 
#              var[key]   :  If it is member of dict it will return value
#              if  it not a member of a it will raise key error 
             
#     2. get(key)  :  if  it is member of dict it will return value 
#     if it is not a member it will raise the key error'''

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# print(data['name']) #vaibhav patil 

# #Print (data[percentage]) #key error : perccentage


# #by using get method
# print(data.get('age'))
# print(data.get('percentage')) #none
# print(data.get('percentage','no value'))    #No value 


# '''how to add data into dict
# 1 . Syntax : var[key]  =value 
# '''

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# print(data['name'])

# #Adding a value and key into dict

# data['percentage'] = 89
# print(data)

# ############### Update method ####################

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# data.update(percentage = 89, mobile = 486460539)
# print(data)

# #{'name': 'vaibhav patil', 'age': 26, 'city': 'shegaon', 'percentage': 89, 'mobile': 486460539}

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# data.update(percentage = 89, mobile = 486460539)    
# emp = {'salary': 1000,'emp_id' : 101}
# data.update(emp)
# print(data)

# #{'name': 'vaibhav patil', 'age': 26, 'city': 'shegaon', 'percentage': 89, 'mobile': 486460539, 'salary': 1000, 'emp_id': 101}


# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# print(data['city'])

# #shegaon

# #var[key] = value or var.update(key = value)

# '''How to  update Values in dictionary
# var[key] = value'''

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# print(data['percentage']  = 89

# '''delete data from dict 
#  1. pop()
#  2. popitems()  '''

# data  ={'name' : 'vaibhav patil', 'age' : 26 , 'city': 'shegaon'}
# print(data['percentage']  = 89


#Practice of accessing the dictionary

batch1290 = {101 : {'name' : 'kunal kale', ' course' : ['python','java'],'marks' : {'t1': 67,'t2' : 87}},102 : {'name' : 'kunal kale', ' course' : ['aws','java'],'marks' : {'t1': 77,'t2' : 97}}}

print(batch1290[101] ['name'])
#kunal kale

print(batch1290[101] ['marks']['t2'])
#87

print(batch1290[101]. get('marks'))
#{'t1': 67, 't2': 87}


##practice  for adding data

batch1290[101]['age' ]= 26
print(batch1290)











