#1. Create a list and perform the following methods 1) insert() 2) remove() 3)
#append() 4) len() 5) pop() 6) clear()

# list = [1, 2, 3, 4, 5, 6, 7,]

# list.insert(2,10)
# list.remove(5)
# list.append(20)
# list.__len__()
# list.pop(4)
# list.clear()
# print(list)

#2. Create a dictionary a nd apply the following methods 1) Print the dictionary
#items 2) access items 3) use get() 4)change values 5) use len()

# dict = {"first_name":"Aditi", "last_name":"Amit","Age":26}
# print(type(dict))
# print(dict.items())
# print(dict.keys())
# print(dict.values())
# print(len(dict))
# print(dict.get("Age"))
# dict["Age"] = 22
# print(dict)

# 3 Create a tuple and perform the following methods 1) Add items 2) len() 3)
#check for item in tuple 4)Access items.
#
# t = (1, 2, 3, 4, 5, 6)
# print(t)
# print(len(t))
# l=list(t)
# print(l)
# print(type(t))

# 4 Write a python program to print a number is positive/negative using if-else

# num1 = int(input("enter the  number ="))
# if num1 >=0:
#     print("number is positive",num1)
# elif num1 <=0:
#     print("number is negetive", num1)
# else:
#      print(" the num is invalid")


#5. Write a python program to find largest number among three numbers.

# num1 = int(input("enter the 1 number="))
# num2 = int(input("enter the 2 number="))
# num3= int(input("enter the 3 number="))

# if num1>num2 and num1>num3:
#     print("largest num is =",num1)
# elif num2>num1 and num2>num3:
#     print("largest num is =",num2)
# elif num3 >num1 and num3 >num2:
#     print("largest num is =",num3)
# else:
#     print("data is not fount chck value and try again")


# 6 Write a python Program to read a number and display corresponding day
#using if_elif_else?

# day = int(input("enter the day 1 to 7 ="))
# if day == 1:
#     print("the day is sunday ")
# elif day ==2:
#     print("the day is monday")
# elif day ==3:
#     print("the day is tuesday")
# elif day ==4:
#     print("the day wednesday")
# elif day ==5:
#     print("the day is thursday")
# elif day ==6:
#     print("the day is friday")

#  7. Write a program to create a menu with the following options 1. TO PERFORM
# ADDITITON 2. TO PERFORM SUBTRACTION 3. TO PERFORM MULTIPICATION
# 4. TO PERFORM DIVISION Accepts users input and perform the operation
# accordingly. Use functions with arguments
#
# num1= int(input("enter the num="))
# num2= int(input("enter the num="))
# arithmatic_operation = input("enter the arithamatic operation = ")
# if arithmatic_operation =="+":
#     res= num1+num2
# elif arithmatic_operation =="-":
#     res = num1 -num2
# elif arithmatic_operation =="*":
#     res = num1*num2
# elif arithmatic_operation =="/":
#     res = num1/num2
# print(res)

#8 Write a python program to find factorial of a given number

# num=5
# fact = 1
# for i in range(1,num+1):
#     fact = fact*i
# print("the num is fact =",fact)

# 9. Write a Python program that takes two lists and returns True if they are
# equal otherwise false.

# lst = [1, 2, 3, 4, 5]
# lst1 = [1, 2, 3, 4, 5]
#
# if lst == lst1:
#     print("true")
# else:
#     print("false")


# 10 Write a program to create a new string made of an input string’s
# first, middle, and last character.

# str1=("aditi")
# a= str1[0]
# b=len(str1)
# mid_char = int(b/2)
# print(a+str1[mid_char]+str1[-1])

#11 Write a program to create a new string made of the middle three
# characters of an input string.

# str = "samrudhi"
# a = len(str)
# mid_char = int(len(str)/2)
# res= str[mid_char -1 : mid_char +2]
# print(res)

#12 Given two strings, s1 and s2. Write a program to create a new
# string s3 by appending s2 in the middle of s1.

# s1 =" hello"
# s2 = "amita"
# mid_char = int(len(s1)/2)
# s3= s1[:mid_char]+s2
# res = s3 + s1[mid_char:]
# print(res)


#  13 given string contains a combination of the lower and upper case
#letters. Write a program to arrange the characters of a string so that all
#lowercase letters should come first.

# str= "jambHULkAr"
# lower = []
# upper = []
# for i in str:
#     if i.islower():
#         lower.append(i)
#     elif i.isupper():
#         upper.append(i)
# res = lower + upper
# print(res)

# 14 Count all letters, digits, and special symbols from a given string

# str1 = "duGui@sGoodBoy25"
# letter = 0
# digit_count=0
# special_char=0
# for i in str1:
#     if i.isalpha():
#         letter +=1
#     elif i.isnumeric():
#         digit_count +=1
#     else:
#         special_char+=1
#         pass
# print("the number of char in str =",letter)
# print('the number of digit in char  =',digit_count)
# print("the num of special char is =",special_char)

#15 Given two strings, s1 and s2. Write a program to create a new string
# s3 made of the first char of s1, then the last char of s2, Next, the second
# char of s1 and second last char of s2, and so on. Any leftover chars go at
# the end of the result.

# str = "hello"
# str1 = "aditi"
# for x,y in zip(str,str1[::-1]):
#     res= x+y
#     print(res, end= ' ')

