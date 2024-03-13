# 1. Write a program that reads a string from keyboard and prints the unique words. Your
# program should convert input string to lower case.

# string = input('Enter a string: ').lower()
# words = string.split()
# print(words)

# 2 Write a program to print all elements in a list those have only single occurrence.
# Example: if contents of list is [7, 5, 5, 1, 6, 7, 8, 7, 6]

# dict = []
# list = [7, 5, 5, 1, 6, 7, 8,  7, 6]
#
# for value in list:
#     if not value in dict:
#         dict+= 1
#     else:
#         dict += 1
# print(dict)

# 4 Write a program to read 6 numbers and create a dictionary having keys EVEN and ODD.
# Dictionary's value should be stored in list. Your dictionary should be like

# dic = {}
# even = []
# odd = []
# for i in range(0,7):
#
#     if i % 2 == 0:
#         even.append(i)
#     else:
#        if i % 2 ==1:
#         odd.append(i)
# dic = {}
# dic['even']= even
# dic['odd']=odd
# print(dic)


# 7  Write a Python program that prompts the user to enter a positive integer.
# Your program should display all the factors of the number.
# Additionally, calculate and display the sum of its factors.
#
# num = int(input("Enter a positive integer: "))
# factor = 0
# sum=0
# print("Factors=", end=" ")
# for i in range(1, num + 1):
#     if num % i == 0:
#         print(i, end=" ")
#         sum= sum+i
# print("\n","the sum of positive integer =",sum)


# 10 Write a program to enter the numbers till the user wants and at the end
# it should display the count of positive, negative and zeros entered.

# positive_count = 0
# negative_count = 0
# zero_count = 0
# choice = "y"
# while choice =="Y" or choice=='y':
#     num = int(input("Enter a number: "))
#     if num == 0:
#          zero_count += 1
#     elif num > 0:
#          positive_count += 1
#     else:
#         negative_count +=1
#
#     choice = input("do you want continue?(y/n)")
# print("positiv count=",positive_count)
# print("negative count=",negative_count)
# print("zero count=",zero_count)


# 8
# sum=0
# while True:
#     num= int(input("enter the num ="))
#     if num < 0:
#         break
#     else:
#         sum= sum + num
# print(sum)

# 9 Write a program that uses a loop to repeatedly ask the user to enter integers. The
# loop will come to an end when zero is entered. After collecting all the integers, the
# program will compute and display the average of all the entered numbers.

# sum=0
# count = 0
# while True:
#     num= int(input("enter the num ="))
#     if num == 0:
#         break
#     else:
#         sum= sum + num
#         count= count +1
# res = sum/count
# print(res)

# 11 Write a program to enter the numbers till the user wants and at the end the
# program should display the largest and smallest numbers entered.
#
# smallest_one = 9999
# largest_one= 0
# choice = "y"
# while choice =="Y" or choice=='y':
#     num = int(input("Enter a number: "))
#
#     if num >largest_one:
#          largest_one = num
#     elif num <= smallest_one:
#         smallest_one = num
#     choice = input("do you want coontinue?(y/n)")
# print("largest num ",largest_one)
# print("smallest num",smallest_one)

# 12 . Write a program that asks the user to input a positive integer. Your program should
# find and display the sum of digits of number. For example, sum of digits of number
# 32518 is 3+2+5+1+8 = 19.

# num = int(input("enter the num = "))
# sum = 0
# temp= num
# while temp > 0:
#     digit = temp % 10
#     sum = sum + digit
#     temp = temp // 10
# print(sum)

# 13 Write a program to obtain the first 25 numbers of a Fibonacci sequence. In a
# Fibonacci sequence the sum of two successive terms gives the third term. Following are
# the first few terms of the Fibonacci sequence:
# 0 1 1 2 3 5 8 13 21 34 55 89

# num = int(input("enter the num ="))
# a = 0
# b = 1
# for i in range(0, num):
#     print(a,end= " ")
#     c = a + b
#     a = b
#     b = c


# 14 . Write a program that generates a random number and asks the user to guess what
# the number is. If the user's guess is higher than the random number, the program
# should display "Too high, try again." If the user's guess is lower than the random
# number, the program should display "Too low, try again." The program should use a
# loop that repeats until the user correctly guesses the random number. Program should
# count and display number of tries to win the game

# import random
# guessnum = random.randint(1,100)
# player = 0
# numtry = 0
#
# while player != guessnum:
#     player = int(input("enter the number ="))
#     numtry = numtry +1
#     if player < guessnum:
#          print(" too low")
#     elif player > guessnum:
#          print(" too high")
#     else:
#          print("congrats...")

#15 Write a program that takes an integer input n and prints a pattern using the
# multiplication table from 1 to n. Each cell in the pattern should contain the product of its
# row and column numbers. Here is a sample output:
# Enter a number: 5
# 1 2 3 4 5
# 2 4 6 8 10
# 3 6 9 12 15
# 4 8 12 16 20
# 5 10 15 20 25

# num = int(input("enter the number = "))
# for i in range(1, num+1):
#     for j in range(1,num):
#         print(i*j, end=" ")
#     print()



# dic ={1:5,2:10,3:2,4:7,5:6}
# even =0
# odd =0
# for key,value in dic.items():
#     if key %2 ==0:
#         even += value
#     else:
#         odd += value
# print(even)
# print(odd)


