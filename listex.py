#question 1.
students  =["adarsh","atharv","shubham","omakr","vivek","nilesh","pritam","swaraj","shrinu"]
print(students[3])
print(students[4:7:1])
print(students[-3:-8:-2])
print(students[-3:])
print(students[2][:-2])
print(students[3][:2])

#question 2

numbers = [10,20,30,40,[11,22,33,44,55,[1,2,3,4,5,6,7],66,77],50,60,70]
print(numbers)

print("To access 30 : ",numbers[2])
print("To access 50 : ",numbers[5])
print("To access 33 : ",numbers[4][2])
print("To access 77 : ",numbers[4][7])
print("To access 3 : ", numbers[4][5][2])


numbers = [10,20,30,40,[11,22,33,44,[1,2,33,4,5,6],55,22,66,77,88],50,60,70]

print(numbers[:-4:-1])
numbers[4][2] = 20
print(numbers)
numbers[4].pop(-4)
numbers[4][4].insert(-2,999)
print(numbers)
print(numbers[4][4][3: :1])
numbers[4][4][1: :2] = [22,44,66]
print(numbers)

