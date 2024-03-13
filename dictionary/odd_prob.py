# dic={1:20,2:30,3:40}


# for k,v in dic.items():
#     sum = 0
#     if k % 2!= 0:
#         sum= sum + v
#
# print("the sum of odd keys value=", sum)


# dic={1:20,2:30,3:40}
#
# for k in dic.values():
#     print(k)

# dic={1:20,2:30,3:40}
# for v in dic.keys():
#     print(v)

# dic ={}
# dic ["firstname"]=input('enter the name=')
# dic ["age"]=int(input("enter the name="))
# print(dic)

# dic ={}
# dic ["firstname"]=input('enter the name=')
# dic ["age"]=int(input("enter the name="))
# print(dic)
# age=int(input("enter the name of update="))
# dic["age"] =age
# print(dic)



# Write a Python program to prompt user to enter 6 subject marks and
# student name in different dictionaries to calculate percentage of
# student’s 6 subject marks list stored in dictionary as a value and and
# another dictionary has student name as value by using this calculate
# total and percentage and display Topper.
# Example :- Sub_Mark={1:[89,75,90,45,67,79], 2:[67,87,97,45,85,73],
# 3:[88,45,65,86,82,55], 4:[77,65,91,89,73,66], 5:[90,87,67,75,88,79]}
# Stud_dict={1:”Ram”, 2:”Shyam”, 3:”Radha”, 4:”Gauri”, 5:”Shiv”}

# Sub_Mark={1:[89,75,90,45,67,79], 2:[67,87,97,45,85,73],
# 3:[88,45,65,86,82,55], 4:[77,65,91,89,73,66], 5:[90,87,67,75,88,79]}
#
# Stud_dict={1:"ram", 2:"shyam", 3:"radha", 4:"gauri", 5:"shiv"}
# dic = {}



#  Write a program to crate function to find the two numbers whose
# product is maximum among all the pairs in a given set of numbers.
# ( Use the Python set).
# Example – Input 1 - [1, 2, 3, 4, 5, 6, 7, 8, 9]
#  Output – (8,9)
#  Input 2- [1, -2, -3, 4, 5, -6, 7, -8, 9]
#  Output – (7,9


# def find_max(numbers):
#     max_pair = None
#     num1 = set(numbers)
#     for num in num1:
#         for other_num in num1:
#             if num != other_num:
#                 product = num * other_num
#                 if product > max_product:
#                     max_product = product
#                     max_pair = (num, other_num)




# Write a program to prompt the user to enter Signal color and display to
# action to perform.Store data into dictionary in the from of key value pair
# Example :-
# Color Action
# Red   Stop the Vehicle.
# Yellow   To wait or go slow.
# Green   Vehicles are allowed to go ahead.
# White   follow the car in front of them
#
# dict = {"red":"stop the vehicle", "yellow":"to wait or go ", "green":"vehicle are allowed to go ahead",
#         "white":"follow the car in front of them"}
# colour =input("enter the signal =")
#
# if colour in dict:
#     print(dict[colour])