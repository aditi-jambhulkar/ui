# 1  .Write a program which will find all such numbers which are divisible by 7 but are
# not a multiple of 5, between 2000 and 3200 (both included).
# The numbers obtained should be printed in a comma-separated sequence on a single line.

# list =[]
# for i in range(2000,3200):
#     if (i % 7 ==0 and i % 5 != 0):
#         print(i , end=' ')


# 2  With a given integral number n, write a program to generate a dictionar that contains (i, i*i)
# such that is an integral number between 1 and n (both included). and then the program should print the dictionary.
# Suppose the following input is supplied to the program:
# 8
# Then, the output should be:
# {1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64}

# n=int(input( "enter the num ="))
# d=dict()
# for i in range(1,n+1):
#     d[i]=i*i
# print(d, end= ' ')


# 3.Write a program that calculates and prints the value according to the given formula:
# Q = Square root of [(2 * C * D)/H]
# Following are the fixed values of C and H:
# C is 50. H is 30.
# D is the variable whose values should be input to your program in a comma-separated sequence.
# Example
# Let us assume the following comma separated input sequence is given to the program:
# 100,150,180
# The output of the program should be:
# 18,22,24
#
# D = int(input("enter the num ="))
# C = 50
# H = 30
# Q = int((2 * C * D)/ H)** 0.5
# print(Q)

# 4.Write a program that accepts a comma separated sequence of words as input and prints the
# words in a comma-separated sequence after sorting them alphabetically.
# Suppose the following input is supplied to the program:
# without,hello,bag,world
# Then, the output should be:
# bag,hello,without,world


# Write a program, which will find all such numbers between 1000 and 3000 (both included) such that each digit of the number is an even number.
# The numbers obtained should be printed in a comma-separated sequence on a single line.s

# list = []
# for i in range(1000,3000):
#     if i % 2==0:
#         print(i,end=' ,')



#calender

import calendar

# year = 2024
# month = 2

# print(calendar.calendar(2023))
# print(calendar.month(year,month))
# print("the calender of year 2024 is =",year)

from array import *

# a = array('i',[50,25,150,45,15,555])
# print(a[::-1])
# print(type(a))


# write a python program to convert  a list in string

# lst = ['My' , 'name' , 'is' , 'Aditi']
# str = ' '.join(lst)
# print(str)
# print(type (str))

# lst = [1, 3, 5, 7, 2]
# res =str(lst)
# print(res)
# print(type(res))