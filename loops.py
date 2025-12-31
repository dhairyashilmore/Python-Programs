# dict = {}
# for i in range(10):
#     name=input("Enter name :")
#     marks1 =int(input("Enter marks :"))
#     dict[name]= marks1
#     print(dict)
 
# # wap to enter 3 student details using while loop

# data = {}
# while len(data)<3:
#       reg  = input("Enter reg no :")
#       name = input("Enter name :")
#       courss=input("Enter course :")
#       data[reg] = {'name':name,'course':courss}
# print(data)

# wap to enter 5 product details using while loop

oppo = {}
add  = 'yes'   
while add=='yes':
      model =(input("Enter model no :"))
      price = int(input("Enter price :"))
      oppo[model] = price
      add =input("do you want to add another yes/no :")
print(oppo)
       