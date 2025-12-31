#1 Wap to calculate circumperance of cirle

Radius  = int(input("Enter a radius of circle : "))
circum =  2 * 3.14 * Radius
print("circumrance of the circle", circum)


#2 Wap to calculate perimeter of Triangle

a = int(input("Enter a side 1 : "))
b = int(input("Enter a side 2 : "))
c = int(input("Enter a side 3 : "))
perimeter = a+b+c
print("The perimeter of triangle",perimeter)


#3 wap to convert to kilometer to meter

KM = int(input("Enter Kilometer : "))
M = KM*1000
print("After convert",KM ,"Kilometer into Meter",M )


#wap to convert to seconds to minitues

Sec = int(input("Enter Seconds : "))

minutes = Sec // 60   
seconds = Sec % 60   

print(f"{Sec} seconds = {minutes} minute(s) and {seconds} second(s)")

#wap to cal avg of three num

a = int(input("Enter a number1 : "))
b = int(input("Enter a number2 : "))
c = int(input("Enter a number3 : "))

total = (a+b+c)/3
print("The average of threen number", total)

#wap to swap to numbers

a = 30
b = 20 
a,b = b,a
print("After swapping two Numbers the value of",a,"and",b )



