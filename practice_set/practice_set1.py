# 1 Write a program that asks the user for his name and then welcomes him. The output
#should look like this:

# name = input("Enter your name: ")
# print("Hello", name)

# 2 Write a program that prompts the user to enter two integers and display their sum on the screen.

# num1 = int(input("Enter first integer= "))
# num2 = int(input("Enter second integer= "))
# sum = num1 + num2
# print("The sum of =",sum)

# 3 Write a program that prompts the user to input a Celsius temperature and outputs the equivalent
# temperature in Fahrenheit.The formula to convert the temperature is: F = 9/5 C + 32
# where F is the Fahrenheit temperature and C is the Celsius temperature.

# celsius = float(input("Enter the temperature in Celsius: "))
# fahrenheit = (9/5)*celsius + 32
# print("The temperature in Fahrenheit is:", fahrenheit)


# 4 Write a program which accept principal, rate and time from user and print the simple interest.
# The formula to calculate simple interest is: simple interest = principal x rate x time / 100
#
# principal =int(input("Enter the principal amount ="))
#
# rate = int(input("Enter the rate of interest="))
#
# time = int(input("Enter the time in years="))
#
# simple_interest = (principal * rate * time) / 100
#
# print("The simple interest is=", simple_interest)


# 5 . Write a program that accepts seconds from keyboard as integer. Your program
# should converts seconds in hours, minutes and seconds. Your output should like this :
# Enter seconds: 13400
# Hours: 3
# Minutes: 43
# Second :20

# second = int(input("enter the second = "))
# hour = second // 3600
# min = (second % 3600)//60
# sec = second % 60
# print("the hour is =",hour)
# print("the min is =",min)
# print("the sec is =",sec)


# 6 Write a program that prompts the user to enter number in two variables and Swap
# the contents of the variables.

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# print("before swap")
# print(num1)
# print(num2)
#
# temp = num1
# num1 = num2
# num2 = temp
# print("after swap")
# print(num1)
# print(num2)

# 7 Write a program that prompts the user to enter number in two variables and Swap
# the contents of the variables.(do not use extra variable)

# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
#
# num1,num2 = num2, num1
#
# print("after swap")
# print(num1)
# print(num2)

# 8 Write a program that prompts the user to input the radius of a circle and
# outputs the area and circumference of the circle. The formula is

# Area = pi x radius2
# Circumference = 2 x pi x radius

# radius = float(input("Enter the radius of the circle: "))
# area = 3.14 * radius * radius
# circumference = 2 * 3.14 * radius
# print("The area of the circle is:", area)
# print("The circumference of the circle is:", circumference)


# 9 . Write a program that prompts the user to input the length and the width
# of a rectangle and outputs the area and perimeter of the rectangle. The
# formula is
# Area = Length x Width
# Circumference = 2 x ( Length + Width)

# length = int(input("Enter the length of the rectangle="))
# width = int(input("Enter the width of the rectangle ="))
# area = length * width
# perimeter = 2 * (length + width)
# print("The area of the rectangle is=", area)
# print("The perimeter of the rectangle is=", perimeter)

#10 . Suppose a, b, and c denote the lengths of the sides of a triangle. Then
# the area of the triangle can be calculated using the formula:where
# Write a program that asks the user to input the length of sides of the
# triangle and print the area.

# a = float(input("enter the length of side a ="))
# b = float(input("enter the length of side b ="))
# c = float(input("enter the length of side c ="))
# s = (a+b+c)/2
# area = (s*(s-a) * (s-b) * (s-c)) ** 0.5
# print("the area of triangle",area)

# 11 Write a program which prompts the user to input principal,
# rate and time and calculate compound interest. The formula is : CI = P(1+R/100)^T - P.

# principal = float(input("Enter the principal amount ="))
#
# rate = float(input("Enter the rate of interest ="))
#
# time = float(input("Enter the time in years ="))
#
# compound_interest = principal * ((1 + rate/100) ** time) - principal
#
# print("The compound interest is=", compound_interest)


# 12 Write a python program to find the best of two test average marks out
# of three test’s marks accepted from the user
#
# m1 = int(input("Enter the marks in the first sub= "))
# m2= int(input("Enter the marks in the second sub= "))
# m3= int(input("Enter the marks in the third sub= "))

# if m1<= m2 and m1 <=m3:
#     avg=(m2+m3)/2
# elif m2 <= m3 and m2 <=m1:
#     avg=(m3+m1)/2
# elif m3 <= m1 and m3 <=m2:
#     avg=(m1+m2)/2
# print("the avg mark best of 2 test =",avg)


#13 . Print the sum of the current number and the previous number
# current = 0
# prev = 0
# for i in range(0, 6):
#     current = prev + i
#     print("addition of current number is {} and previous {} is {}".format(i,prev,current))
#     prev = i

# 14 . string that are present at an even index number
# str = input("enter the string =")
# a = len(str)
# for i in range (0,a-1,2):
#     print(str [i])


# 16 Iterate the given list of numbers and print only those numbers which
# are divisible by 5

# lis = [ 2, 5, 6, 7, 10, 17,25 ,30]
# for x in lis:
#     if x % 5 == 0:
#      print(x)


# 15 Write a program to remove characters from a string starting from zero
# up to n and return a new string.

# str = input("enter the string = ")
# num = int(input("enter the num ="))
# res = str[num:]
# print(res)

# 17 Write a program to find how many times substring “Emma” appears in the
#given string.Given:

# str_x = "Emma is good developer. Emma is a writer"
# cnt = str_x.count("Emma")
# print("the times of emma = ",cnt)


# a = "Atul"
# b = "Rakh"
# for x in zip(a,b[::-1]):
#     print(x)


# str = 'python'
# x = list(str)
# for i in x[::2]:
#     print(i)