#25. Write a Python program to create a new dictionary by extracting the
# mentioned keys from the below dic
#
# sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
# keys = ["name", "salary"]
# newdic = {}
# for key in keys:
#     if key in sample_dict:
#         newdic[key] = sample_dict[key]
# print(newdic)


# 26. Delete a list of keys from a dictionary
# Given:
# sample_dict = {"name": "Kelly","age": 25,"salary": 8000,"city": "New york"}
# keys = ["name", "salary"]
# newDic = {}
# for key in sample_dict:
#  if key not in keys:
#   newDic[key] = sample_dict[key]
# print(newDic)


#27. Write a Python program to check if value 200 exists in the following dictionary.
#Given:

# sample_dict = {'a': 100, 'b': 200, 'c': 300}
# if 200 in sample_dict.values():
#     print("present")

# 1 Write a program that prompts the user to input a number and display
# if the number is even or odd

# num = int(input("enter the number ="))
# if num % 2 ==0:
#     print("the num is even")
# else:
#     print("the num is odd")

# 2 Write a Python program that takes an age as input and determines
#whether a person is eligible to vote. If the age is 18 or above, print
#"You are eligible to vote." Otherwise, print "You are not eligible to
#vote yet."

# age = int(input("enter the number ="))
# if age >= 18 :
#     print("you are eligible to vote")
# else:
#     print("you are not eligible to vote")


# 3 . Write a program that prompts the user to input two integers and
# outputs the largest

# a = int(input('enter the first num ='))
# b = int(input("enter the second num = "))
#
# if a>b:
#     print("the gretest num a is =",a)
# elif b>a:
#     print("the gretest num is =", b)
# else:
#     print("invalid")


# 4  Write a program that prompts the user to enter a number and
# determines whether it is positive, negative, or zero. The program
# should print "Positive" if the number is greater than 0, "Negative" if
# the number is less than 0, and "Zero" if the number is 0

# num = int(input(" enter the num ="))
# if num > 0:
#     print(" num is positive")
# elif num < 0:
#     print(" num is negetive")
# else:
#     print( "num is zero")

# 5  Write a program that prompts the user to enter their age and prints the
# corresponding age group. The program should use the following age groups:
# 0-12: Child
# 13-19: Teenager
# 20-59: Adult
# 60 and above: Senior Citizen

# age = int(input("enter the age = "))
# if age <= 12:
#     print("chid")
# elif age <= 19:
#     print("teenager")
# elif age <= 59:
#     print("adult")
# elif age <=60:
#     print("senior citizen")
# else:
#     print('invalid')


# 6  Write a program that prompts the user to input a number from 1 to 7.
# The program should display the corresponding day for the given
# number. For example, if the user types 1, the output should be
# Sunday. If the user types 7, the output should be Saturday. If the
# number is not between 1 to 7 user should get error message as
# shown in sample output.

# day = int(input("enter the day 1 to 7 ="))
# if day == 1:
#     print("the day is sunday ")
# elif day ==2:
#     print("the day is monday")
# elif day ==3:
#     print("the dsy is tuesday")
# elif day ==4:
#     print("the day wednesday")
# elif day ==5:
#     print("the day is thursday")
# elif day ==6:
#     print("the day is friday")


# 7. Write a program that prompts the user to enter their weight (in kilograms) and
#height (in meters). The program should calculate the Body Mass Index (BMI)
#using the formula: BMI = weight / (height * height). The program should then
#classify the BMI into one of the following categories:

#less than 18.5 - Underweight
#BMI between 18.5 and 24.9 - Normal weight
#BMI between 25 and 29.9 - Overweight
#BMI 30 or greater – Obesity

# weight = int(input("enter the weight in kg = "))
# height = float(input("enter the height in meter ="))
# BMI = weight / (height * height)
# if BMI < 18.5:
#     print("underweight")
# elif BMI <=24.9:
#     print("normal weight")
# elif BMI <= 29.9:
#     print("overweight")
# else:
#     print("obsity")

# 8. The marks obtained by a student in 3 different subjects are input by the user. Your
# program should calculate the average of subjects and display the grade. The student
# gets a grade as per the following rules:
# Average Grade
# 90-100 A
# 80-89 B
# 70-79 C
# 60-69 D
# 0-59 F
#
# s1 = int(input("enter the marks sub ="))
# s2 = int(input("enter the marks sub ="))
# s3 = int(input("enter the marks sub ="))
#
# total = s1+s2+s3
# avg = total/3
# print("the total mark = ",total)
# print("the avaerage =",avg)
# if avg  >= 90 and avg >= 100:
#     print("a class")
# elif avg >= 80 and avg >= 89:
#     print("b class")
# elif avg >= 70 and avg >=79:
#     print("c class")
# elif avg  >= 60 and avg >= 69:
#     print("d class")
# elif avg >= 0 and avg >= 59:
#     print("f class")
# else:
#     print("invalid")

# 9 Write a program that prompts the user to enter three numbers and sorts
#them in ascending order. The program should print the sorted numbers.
#
# num1 = int(input("Enter the first number: "))
# num2 = int(input("Enter the second number: "))
# num3 = int(input("Enter the third number:"))
#
# result = sorted([num1,num2,num3])
# print("Sorted numbers in ascending order:", result)

# 10 Write a program that prompts the user to input a character and determine
# the character is vowel or consonant.

# letter = input("Enter a letter: ")
# vowel= ('a','e','i','o','u')
# if letter in vowel:
#     print(" is a vowel.")
# else:
#     print("is a consonant.")


# 11 . Write a program that prompts the user to input a year and determine whether the
# year is a leap year or not.
# Leap Years are any year that can be evenly divided by 4. A year that is evenly divisible by
# 100 is a leap year only if it is also evenly divisible by 400. Example :
# 1992 Leap Year
# 2000 Leap Year
# 1900 NOT a Leap Year
# 1995 NOT a Leap Year

# year = int(input("Enter a year : "))
# if year % 4 == 0:
#     print(year,"is a leap year")
# elif year % 100 == 0:
#         print( year,"is a leap year")
# elif year % 400 == 0:
#         print(year,"is a leap year")
# else:
#         print(year, "is not a leap year")


# 12. Write a program that prompts the user to input number of calls and
# calculate the monthly telephone bills as per the following rule:
# Minimum Rs. 200 for up to 100 calls.
# Plus Rs. 0.60 per call for next 50 calls.
# Plus Rs. 0.50 per call for next 50 calls.
# Plus Rs. 0.40 per call for any call beyond 200 calls

# calls = int(input("Enter number of calls: "))
# #
# if calls <= 100:
#     bill = 200
# elif calls > 100 and calls <= 150:
#     calls = calls - 100
#     bill = 200 + (0.60 * calls)
# elif calls > 150 and calls <= 200:
#     calls = calls - 150
#     bill = 200 + (0.60 * 50) + (0.50 * calls)
# else:
#     calls = calls - 200
#     bill = 200 + (0.60 * 50) + (0.50 * 50) + (0.40 * calls)
#
# print("Total bill amount is", bill)


# 13 . Write a program to iterate the first 10 numbers, and in each iteration, print
# the sum of the current and previous number.
# i = 0
# previous = 0
# for i in range (0, 6):
#     sum = previous +i
#     print(sum)
#     previous = i

# 14 Write a program to add two lists index-wise. Create a new list that contains
# the 0th index item from both the list, then the 1st index item, and so on till the
# last element. any leftover items will get added at the end of the new list.
#
# list = ["p", "y","t", "h","o","n"]
# list1 = [ "j", "a","v","a"]
# for x,y in zip(list,list1):
#     print(x,y)

#15 . Given a list of numbers. write a program to turn every item of a list into its
#square

# list = [1, 2, 3, 4, 5, 6,7]
# for i in list :
#     print(i*i)

# 16. Concatenate two lists in the following order
# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
# Expected output:
# ['Hello Dear', 'Hello Sir', 'take Dear', 'take Sir'

# list1 = ["Hello ", "take "]
# list2 = ["Dear", "Sir"]
#
# for x in list1:
#     for y in list2:
#         print(x+" "+y)

# 17 . Given a two Python list. Write a program to iterate both lists simultaneously
# and display items from list1 in original order and items from list2 in reverse order

# list1 = [10, 20, 30, 40]
# list2 = [100, 200, 300, 400]
# for x, y in zip(list1, list2[::-1]):
#     print(x, y)

#18 . Write a python program that remove empty strings from the list of strings
# list1 =['mike','','emma','kelly','','brad']
# result = list(filter(None,list1))
# print(result)


#19 Write a program to add item 7000 after 6000 in the following Python List
# Given:
# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# Expected output:
# [10, 20, [300, 400, [5000, 6000, 7000], 500], 30, 40]

# list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
# (list1[2][2].append(7000))
# print(list1)

#21 you have given a Python list. Write a program to find value 20 in the list, and
# if it is present, replace it with 200. Only update the first occurrence of an item.
# list = [ 5, 20, 15, 20, 25, 50, 20]
# ind = list.index(20)
# list[ind]= 200
# print(list)

# 22 Given a Python list, write a program to remove all occurrences of item 20.
# Given:
# list1 = [5, 20, 15, 20, 25, 50, 20]
# while 20 in list1:
#     list1.remove(20)
# print(list1)

# 23. Below are the two lists. Write a Python program to convert them into a
# dictionary in a way that item from list1 is the key and item from list2 is the value

# keys = ['Ten', 'Twenty', 'Thirty']
# values = [10, 20, 30]
# res = dict(zip(keys,values))
# print(res)

# 24 . Merge two Python dictionaries into one
#
# dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
# dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
# marge_dic = dict1.copy()
# marge_dic.update(dict2)
# print(marge_dic)