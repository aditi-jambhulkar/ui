#Exercise 1: Define a function that accepts 2 values and
# return its sum, subtraction and multiplication.

# def sum_sub_add_mul(x,y):
#     sum = x+y
#     sub = x-y
#     mul = x*y
#     return sum,sub,mul


# 2 Define a function that accepts roll number and returns whether the student is present or absent.

# def present_absent(roll_no):
#     list = [2,3,4,5,6,7,8,9,10]
#     if roll_no in list:
#         print("present")
#     else:
#         print("absent")

#Exercise 3: Define a function in python that accepts 3 values and returns the maximum of three numbers.
# def max( x, y, z):
#     if x >=y and x >=z:
#         print("max", x)
#     elif y >= z and y >=x:
#         print("max", y)
#     elif z >= x and z >= y:
#         print("max", z)



# Exercise 4: Define a function that accepts a number and returns whether the number is even or odd.
# def even_odd(*args):
#     for a in args:
#       if a % 2 ==0:
#         print("the number is even",a)
#       else:
#         print("the number is odd",a)

#Exercise 5: Define a function which counts vowels and consonant in a word.
# def vowels_consonant(val):
#     vowels = 0
#     cons = 0
#     for i in range(len(val)):
#         if val[i] in ["a","e","i","o","u"]:
#             vowels = vowels + 1
#         else:
#
#             cons += 1
#
#     print("the num of vowels =",vowels)
#     print("the cons =",cons)


#Exercise 6: Define a function that returns Factorial of a number.

# def fact(num1):
#     fact =1
#     for i in range(1, num1 +1):
#         fact = fact *i
#     return fact

# Define a function that accepts lowercase words and returns uppercase words.
# def lowercase_uppercase(str1):
#     res = str1.upper()
#     return res


#Exercise 8: Define a function that accepts radius and returns the area circle.

# def radious_of_circle(r):
#     area = 3.14*r*r
#     return area

# def animal_cracker(str):
#     word = str.split()
#     if (word[0][0] ==word[1][0]):
#         return True
#     else:
#         return False

# def less_greater(a,b):
#     if a%2 == 0 and b % 2== 0:
#         return min(a,b)
#     else:
#         return max(a,b)

# given two int return true if sum int 20 or one int 20, other wise false

# def make_20(a,b):
#     if a+ b == 20 or a==20 or b== 20:
#         return True
#     else:
#         return False


#  captalization 1 word and 4 word
# def capword(name):
#     return name[0].upper()+ name[1:3] + name[3].upper() +name[4:]


    # only reverse the word

# def revers_word(str):
#     lst = str.split()[::-1]
#     newstr = ' '.join(lst)
#     return newstr

# given return true if n is within 10 of either  100,200

# def almost_there(n):
#     if abs(100-n) <= 10 or abs(200-n)<= 10:
#         return True
#     else:
#         return False

# return a string where for every character in the orignal string

# def repeat_char(str):
#     result = ''
#     for char in str:
#         result = result + char * 3
#     return result


# calculate sphere
# def sphere(rad):
#     return (4/3)*(3.142)*(rad**3)

# check given no is in range
# def check_range(no,low,high):
#     if no in range(low,high+1):
#         return 'no is in range'
#     else:
#         return 'no is not i range'


# count uppercase lowercase letter in str
# def countletter(str):
#     upper = 0
#     lower = 0
#     for char in str:
#         if char.upper():
#             upper = upper+1
#         else:
#             lower = lower + 1
#     print("total upper = {} and lower = {}".format(upper,lower))


