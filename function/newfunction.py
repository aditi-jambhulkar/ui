# check prime no

# def check_prime(no):
#     num =0
#     for x in range(2,no):
#         if no % x == 0:
#             num=1
#     if num == 0:
#         print("prime no")
#     else:
#         print('not prime')
#
# check_prime(1)

# check str pallindrom or not
# def pallindrome(str):
#     s = str[::-1]
#     if s == str:
#         return  "pallindrome string"
#     else:
#         return "not pallindrome"
#
# a = pallindrome('madam')
# print(a)

# to mul all num in list

# def mulitem(lst):
#     ans = 1
#     for x in lst:
#         ans = ans * x
#     return ans

# a = mulitem([1,2,3,4,5])
# print(a)

# check a list and return unique element

# def unique(lst):
#     x = []
#     for item in lst:
#         if item not in x:
#             x.append(item)
#     return x
#
# a = unique([1,1,2,3,4,5,4,6,5])
# print(a)